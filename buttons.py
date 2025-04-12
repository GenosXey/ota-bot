# app/handlers/buttons.py

from pyrogram import Client, filters
from pyrogram.types import Message
from app.db import get_user, get_points, get_referral_count

def register_handlers(bot: Client):
    
    @bot.on_message(filters.text("MINES PRREDICTION"))
    async def mines_prediction(_, message: Message):
        await message.reply(
            "✅✅✅ SIGNAL FAIT ✅✅✅\n\n"
            "💣 Mines : 3\n"
            "⏰ Validité : 2mn\n"
            "🔄 Nombre de tentatives : 3\n\n"
            " 🔗 Jouez Ici  ▎ Играйте здесь (https://1wzvro.top/casino/play/1play_1play_mines)\n\n"
            "🟦🟦🟦⭐️⭐️\n"
            "🟦🟦🟦🟦🟦\n"
            "🟦🟦🟦🟦🟦\n"
            "🟦🟦🟦🟦🟦\n"
            "🟦🟦🟦⭐️⭐️\n\n"
            "⁉️Comment jouer : https://t.me/mines1winoriginals/133\n\n"
            "⚠️Remarque : Il est conseillé de miser des sommes considérables.\n"
            "Les signaux Mines founis par le bot sont plus sûrs avec les comptes créés avec le code promo MINE64 !"
        )

    @bot.on_message(filters.text("MON LIEN"))
    async def mon_lien(_, message: Message):
        user = get_user(message.from_user.id)
        ref_link = f"https://t.me/KingfoBot?start={message.from_user.id}"
        referrals = get_referral_count(message.from_user.id)
        await message.reply(
            "🚀 Copier et partager ce lien dans des groupes, canaux, sur des réseaux sociaux. "
            "Lorsqu'une personne clique sur votre lien et l'utilise, vous recevrez une récompense de +3 points directement dans ce bot.\n\n"
            f"💹 Votre Lien : {ref_link}\n\n"
            f"🎯 Vous avez invité : {referrals} Utilisateurs"
        )

    @bot.on_message(filters.text("📉 Regle de jeu"))
    async def regle_jeu(_, message: Message):
        await message.reply(
            "Comment commencer à gagner de l'argent ! 🚀\n\n"
            "1. Créez votre compte - La première étape consiste à créer votre compte sur 1Win. "
            "C'est le seul site de paris en qui je fais confiance et le seul où mes signaux fonctionnent ! "
            "✅ Pour créer votre compte, cliquez simplement sur ce lien : "
            "[🔥500% BONUS 🔥](https://1wzvro.top/casino/list?open=register&p=rzv9) et remplissez vos informations. "
            "N'oubliez surtout pas d'utiliser le code promo MINE64\n\n"
            "2. Dépôt - Après avoir créé votre compte, il ne vous reste plus qu'à effectuer votre dépôt. "
            "✅ Sur la plateforme 1Win, cliquez simplement sur le bouton « FAIRE UN DEPOT ». "
            "✅ Ils acceptent différents modes de paiement, vous n'aurez donc aucun problème ! ✅\n\n"
            "3. Gagnons de l'argent ! - Après avoir effectué votre dépôt, gagnons maintenant de l'argent 😍 "
            "Tout d'abord, vous devez trouver le jeu Mines dans 1Win 🏆 "
            "Suivez les étapes de la vidéo ci-dessous (cliquez simplement sur la vidéo)\n\n"
            "Fait! - Prêt, il ne vous reste plus qu'à gagner de l'argent avec nous ! ✅\n\n"
            "☎️ Si vous avez des questions, n'hésitez pas à me contacter en support : @CyberrXGhost",
            parse_mode="HTML"
        )

    @bot.on_message(filters.text("COMPTE 🧑‍💻"))
    async def compte(_, message: Message):
        user = message.from_user
        points = get_points(user.id)
        await message.reply(
            f"💳 Nom d'utilisateur : {user.first_name}\n\n"
            f"🚀 Signaux : {points} points\n\n"
            f"🏷 ID : {user.id}\n\n"
            f" 📖 Langue : fr"
        )

    @bot.on_message(filters.text("📞 Aide"))
    async def aide(_, message: Message):
        await message.reply(
            "Si vous rencontrez un problème majeur, vous pouvez contacter directement le propriétaire - @CyberrXGhost\n"
            "L'achat des signaux aussi est disponible."
        )
