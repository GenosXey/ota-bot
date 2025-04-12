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

├── app/                           
│   ├── handlers/                 
│   │   ├── start.py               
│   │   ├── buttons.py               
│   │   ├── callback.py             
│   │   └── bonus.py                 
│   │
│   ├── db.py                      
│   ├── keyboards.py                
│   └── config.py                   
│
├── main.py                          
├── requirements.txt                
├── Procfile                       
└── README.md                       


## 🚀 Déploiement sur Koyeb

1. Crée une app Python
2. Ajoute les variables d’environnement :

```env
API_ID=xxxx
API_HASH=xxxxxxxxxxxxxxxx
BOT_TOKEN=123456:ABCDEF
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/mydb
