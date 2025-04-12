# app/handlers/callback.py

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

def register_handlers(bot: Client):

    @bot.on_callback_query(filters.regex("click_btn"))
    async def handle_click_btn(client: Client, callback_query: CallbackQuery):
        await callback_query.message.reply(
            "Salut comment ça va ? partage le lien pour gagnez des points"
        )
        await callback_query.answer()  # ferme le loader côté client
