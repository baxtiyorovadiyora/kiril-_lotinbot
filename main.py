# Kiril- Lotin telegram bot/

import telebot
from transliterate import to_cyrillic , to_latin

TOKEN = "YOUR_TOKEN" 
bot = telebot.teleBot(token=TOKEN)

@bot.message_handler(cammands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )
    xabar = f"Asalomu alykum 😊 ,{username} Kiril-Lotin botiga xush kelibsiz !🎀 "
    xabar += "/n Matiningizni kiriting☝️."
    bot.reply_to(message, xabar)

    bot.polling
    
