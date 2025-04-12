# app/config.py

import os

API_ID = int(os.getenv("API_ID", "12345678"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# MongoDB URI (ex: mongodb+srv://user:pass@cluster0.mongodb.net/myDB)
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_connection_uri")
DB_NAME = "kingfobot"
