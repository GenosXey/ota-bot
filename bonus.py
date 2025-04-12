# app/handlers/bonus.py

from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, timedelta
from app.db import users_col

BONUS_AMOUNT = 50

def register_handlers(bot: Client):

    @bot.on_message(filters.command("bonus"))
    async def bonus_handler(client: Client, message: Message):
        user_id = message.from_user.id
        user = users_col.find_one({"_id": user_id})

        now = datetime.utcnow()
        last_bonus = user.get("last_bonus")

        if last_bonus:
            last_bonus_time = datetime.strptime(last_bonus, "%Y-%m-%dT%H:%M:%S")
            if now - last_bonus_time < timedelta(days=7):
                remaining = (last_bonus_time + timedelta(days=7)) - now
                hours = remaining.total_seconds() // 3600
                await message.reply(
                    f"⏳ Vous avez déjà réclamé votre bonus.\n"
                    f"Revenez dans {int(hours)} heures pour recevoir vos 50 signaux."
                )
                return

        users_col.update_one(
            {"_id": user_id},
            {
                "$inc": {"points": BONUS_AMOUNT},
                "$set": {"last_bonus": now.strftime("%Y-%m-%dT%H:%M:%S")}
            }
        )

        await message.reply(f"🎁 Vous venez de recevoir {BONUS_AMOUNT} signaux gratuits ! Profitez-en bien ✅")
