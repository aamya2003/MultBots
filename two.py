import telebot


bot2 = telebot.TeleBot("")


@bot2.message_handler()
def sayImTow(message):
    bot2.send_message(message.chat.id, "I'm Two")
