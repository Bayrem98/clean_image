<div align="center">

<img src="docs/banner.svg" alt="Clean Image banner" width="100%"/>

# 🖼️ Clean Image

**Application web de suppression d'objets dans les images, propulsée par IOPaint & LaMa.**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![IOPaint](https://img.shields.io/badge/IOPaint-LaMa-ff6f00)](https://github.com/Sanster/IOPaint)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Bayrem98/clean_image/pulls)

[Fonctionnalités](#-fonctionnalités) •
[Installation](#-installation) •
[Utilisation](#-utilisation) •
[Structure](#-structure-du-projet) •
[Dépannage](#-dépannage)

</div>

---

## ✨ Fonctionnalités

- 🧹 **Suppression d'objets** : effacez n'importe quel élément d'une image en le masquant.
- 🎨 **Inpainting** : reconstruction automatique du fond par le modèle **LaMa**.
- 🖥️ **Interface web** : UI Flask légère, accessible depuis n'importe quel navigateur.
- ⚡ **CPU-friendly** : fonctionne sans GPU (plus lent, mais 100 % local).
- 🔒 **Confidentialité totale** : aucune image n'est envoyée à un serveur externe.

---

## 🛠️ Stack technique

| Composant | Rôle |
|---|---|
| [IOPaint](https://github.com/Sanster/IOPaint) | Moteur d'inpainting |
| [LaMa](https://github.com/advimman/lama) | Modèle de deep learning (Samsung AI) |
| [Flask](https://flask.palletsprojects.com/) | Serveur web / API |
| [PyTorch](https://pytorch.org/) | Framework deep learning |
| HTML / CSS / JS | Frontend |

---

## 📋 Prérequis

- **Python 3.12**
- **pip** à jour
- Windows / Linux / macOS
- ~2 Go d'espace disque (modèle LaMa + dépendances)

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Bayrem98/clean_image.git
cd clean_image
```

### 2. Créer un environnement virtuel

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD)**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Utilisation

### Étape 1 — Lancer le moteur IOPaint

Dans un **premier terminal** (venv activé) :

```bash
iopaint start --model=lama --device=cpu --port=8080
```

**Options disponibles :**

| Option | Description | Valeurs |
|---|---|---|
| `--model` | Modèle d'inpainting | `lama`, `ldm`, `zits`, `manga` |
| `--device` | Périphérique de calcul | `cpu`, `cuda`, `mps` |
| `--port` | Port du serveur | ex. `8080` |

> ⏳ **Premier lancement** : le modèle LaMa (~200 Mo) est téléchargé automatiquement dans `~/.cache/`. Cela peut prendre plusieurs minutes.

### Étape 2 — Lancer l'application Flask

Dans un **second terminal** (venv activé) :

```bash
python app.py
```

Puis ouvrez 👉 **http://localhost:5000**

### Étape 3 — Utiliser l'application

1. **Uploadez** une image.
2. **Dessinez** un masque sur les objets à supprimer.
3. **Cliquez** sur *Supprimer* → résultat en quelques secondes.
4. **Téléchargez** l'image nettoyée.

---

## 📁 Structure du projet

```
clean_image/
├── app.py                  # Application Flask principale
├── templates/
│   └── index.html          # Interface web
├── downloads/              # Images uploadées / traitées (gitignore)
├── docs/
│   └── banner.svg          # Bannière du README
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

## ⚙️ Configuration

Variables d'environnement optionnelles, dans un fichier `.env` :

```env
IOPAINT_HOST=http://127.0.0.1:8080
FLASK_PORT=5000
FLASK_DEBUG=True
```

---

## 🐛 Dépannage

| Problème | Solution |
|---|---|
| `iopaint: command not found` | Vérifiez que le venv est activé et que `pip install -r requirements.txt` a réussi |
| `CUDA out of memory` | Utilisez `--device=cpu` |
| Port déjà utilisé | Changez le port (`--port=8081`) |
| Modèle bloqué au téléchargement | Vérifiez votre connexion ; le cache est dans `~/.cache/` |
| Erreur de connexion Flask ↔ IOPaint | Vérifiez que les **deux** serveurs tournent sur les bons ports |

---

## 🗺️ Roadmap

- [ ] Support GPU (CUDA)
- [ ] Choix du modèle depuis l'interface
- [ ] Historique des images traitées
- [ ] Déploiement Docker
- [ ] API REST documentée (Swagger)

---

## 🤝 Contribution

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/ma-fonctionnalite`)
3. Committez (`git commit -m "Add ma fonctionnalite"`)
4. Pushez (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une **Pull Request**

---

## 📄 Licence

Distribué sous licence **MIT**. Voir [`LICENSE`](LICENSE) pour plus de détails.

---

## 👤 Auteur

**Bayrem** — [@Bayrem98](https://github.com/Bayrem98)

Dépôt : [github.com/Bayrem98/clean_image](https://github.com/Bayrem98/clean_image)

---

## 🙏 Remerciements

- [IOPaint](https://github.com/Sanster/IOPaint) par Sanster
- [LaMa](https://github.com/advimman/lama) par Samsung AI
- Tous les contributeurs open-source ❤️

---

<div align="center">

⭐ **Si ce projet vous plaît, laissez une étoile !** ⭐

</div>