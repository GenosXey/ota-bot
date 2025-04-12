# app/config.py

import os

API_ID = int(os.getenv("API_ID", "24817837"))
API_HASH = os.getenv("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7216818057:AAFyHDPbYHFbjVCGBG2Rir7Ai0YMDfGDbiM")

# MongoDB URI (ex: mongodb+srv://user:pass@cluster0.mongodb.net/myDB)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://altof2:123Bonjoure@cluster0.s1suq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = "kingfobot"
