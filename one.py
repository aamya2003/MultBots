import telebot


bot1 = telebot.TeleBot("")


@bot1.message_handler()
def sayImOne(message):
    bot1.send_message(message.chat.id, "I'm One")
