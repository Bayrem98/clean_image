import os
import uuid
import subprocess
import requests
from flask import Flask, render_template, request, jsonify, send_file
from PIL import Image, ImageFilter
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'downloads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def download_file(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers, stream=True, timeout=60)
    r.raise_for_status()
    ctype = r.headers.get('Content-Type', '').split(';')[0].strip().lower()
    return r.content, ctype


def remove_signature_image(img_bytes, box):
    """
    box = (x, y, w, h) en pourcentage (0-1)
    Floute la zone pour effacer la signature.
    """
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    W, H = img.size
    x, y, w, h = box

    left   = max(0, int(x * W))
    top    = max(0, int(y * H))
    right  = min(W, int((x + w) * W))
    bottom = min(H, int((y + h) * H))

    if right <= left or bottom <= top:
        raise ValueError("Zone invalide")

    region = img.crop((left, top, right, bottom))
    blurred = region.filter(ImageFilter.GaussianBlur(radius=40))
    img.paste(blurred, (left, top))

    out = BytesIO()
    img.save(out, format="PNG")
    out.seek(0)
    return out


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    url = (data.get('url') or '').strip()
    box = data.get('box')

    if not url:
        return jsonify({'error': "URL manquante"}), 400

    try:
        raw, ctype = download_file(url)
    except Exception as e:
        return jsonify({'error': f"Téléchargement échoué : {e}"}), 500

    if ctype.startswith('image/'):
        if not box:
            return jsonify({'error': "Zone de signature manquante"}), 400
        try:
            out = remove_signature_image(raw, box)
        except Exception as e:
            return jsonify({'error': f"Erreur image : {e}"}), 500

        filename = f"{uuid.uuid4().hex}.png"
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(path, 'wb') as f:
            f.write(out.read())
        return jsonify({'type': 'image', 'file': filename})

    elif ctype.startswith('video/'):
        ext = os.path.splitext(url.split('?')[0])[1] or '.mp4'
        filename = f"{uuid.uuid4().hex}{ext}"
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(path, 'wb') as f:
            f.write(raw)

        if box:
            try:
                x, y, w, h = box
                vf = (f"drawbox=x=iw*{x}:y=ih*{y}:w=iw*{w}:h=ih*{h}:"
                      f"color=black@0.99:t=fill")
                out_path = os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    f"{uuid.uuid4().hex}_clean{ext}"
                )
                subprocess.run(
                    ["ffmpeg", "-y", "-i", path, "-vf", vf,
                     "-c:a", "copy", out_path],
                    check=True, capture_output=True
                )
                os.remove(path)
                filename = os.path.basename(out_path)
            except Exception as e:
                print("ffmpeg err:", e)

        return jsonify({'type': 'video', 'file': filename})

    else:
        return jsonify({'error': f"Type non supporté : {ctype or 'inconnu'}"}), 400


@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(path):
        return "Fichier introuvable", 404
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)