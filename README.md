# 🤖 KingfoBot – Bot de Prédiction Mines 1Win (Pyrogram + MongoDB)

Un bot Telegram de minage/parrainage écrit en Python avec Pyrogram.

## ⚙️ Fonctionnalités

- Parrainage automatique avec lien (`/start <ref_id>`)
- +5 points au parrain pour chaque filleul
- Commande `/bonus` pour réclamer 50 signaux par semaine
- 5 boutons de menu avec messages automatiques
- Stockage MongoDB (cloud-ready)

## 📂 Structure du projet

KingfoBot/
│
├── app/                            # 📂 Code source du bot
│   ├── handlers/                   # 📂 Tous les gestionnaires de commandes & callbacks
│   │   ├── start.py                # /start + gestion du parrainage
│   │   ├── buttons.py              # Boutons clavier (mines, mon lien, règles, etc)
│   │   ├── callback.py             # Gestion des boutons Inline
│   │   └── bonus.py                # /bonus futur
│   │
│   ├── db.py                       # SQLite handler (création, requêtes utilisateurs)
│   ├── keyboards.py                # Définition des claviers (Inline et Reply)
│   └── config.py                   # Token, API_ID, API_HASH, etc.
│
├── main.py                         # Point d’entrée principal, démarre le bot
├── requirements.txt                # 📦 Dépendances Python
├── Procfile                        # ⚙️ Démarrage automatique sur Koyeb
└── README.md                       # ℹ️ Infos sur le projet


## 🚀 Déploiement sur Koyeb

1. Crée une app Python
2. Ajoute les variables d’environnement :

```env
API_ID=xxxx
API_HASH=xxxxxxxxxxxxxxxx
BOT_TOKEN=123456:ABCDEF
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/mydb
