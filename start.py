# app/handlers/start.py

from pyrogram import Client, filters
from pyrogram.types import Message
from app.keyboards import main_keyboard, inline_click_button
from app.db import create_user
from app.config import API_ID, API_HASH, BOT_TOKEN

START_TEXT = (
    "<b>✨ Bot De prediction du jeu Mine 1win ✅\n\n"
    "🚨 Vous disposez gratuitement et régulièrement de 50 Signaux par semaine a récupérer en appuyant sur 🎁 Bonus (👇) ou /Bonus !</b>\n\n"
    "<i>⚠️Remarque : Les signaux Mines founis par le bot sont sûrs à 100% pour les compte crée avec le code promo MINE64 !</i>"
)

IMAGE_URL = "https://iili.io/3Ys1NiQ.md.jpg"

def register_handlers(bot: Client):

    @bot.on_message(filters.command("start"))
    async def start_command(client: Client, message: Message):
        user_id = message.from_user.id
        username = message.from_user.first_name
        args = message.text.split()

        referred_by = None
        if len(args) > 1:
            ref_code = args[1]
            if ref_code.isdigit() and int(ref_code) != user_id:
                referred_by = int(ref_code)

        create_user(user_id, username, referred_by)

        await message.reply_photo(
            photo=IMAGE_URL,
            caption=START_TEXT,
            reply_markup=inline_click_button,
            parse_mode="html",
        )

        await message.reply("👇 Menu principal :", reply_markup=main_keyboard)
