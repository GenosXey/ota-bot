# main.py

from pyrogram import Client
from app.config import API_ID, API_HASH, BOT_TOKEN
from app.handlers import start, buttons, callback
from app.db import init_db

# Initialise la base de données
init_db()

# Crée l'instance du bot
bot = Client(
    "KingfoBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Enregistre les gestionnaires
start.register_handlers(bot)
buttons.register_handlers(bot)
callback.register_handlers(bot)

# Démarre le bot
if __name__ == "__main__":
    print("🚀 Bot en cours d'exécution...")
    bot.run()
