# app/keyboards.py

from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Clavier principal avec les 5 boutons
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("MINES PRREDICTION")],
        [KeyboardButton("MON LIEN")],
        [KeyboardButton("📉 Regle de jeu")],
        [KeyboardButton("COMPTE 🧑‍💻")],
        [KeyboardButton("📞 Aide")],
    ],
    resize_keyboard=True
)

# Clavier inline pour le bouton « Click »
inline_click_button = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Click", callback_data="click_btn")]]
)
