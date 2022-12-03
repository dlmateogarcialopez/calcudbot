#########################################################
from config import bot
import config
from time import sleep
import re
#########################################################
# Aquí vendrá la implementación de la lógica del bot
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.send_message(
        message.chat.id,
        "Hola, soy un \U0001F929, ¿cómo estás?",
        parse_mode="Markdown") 

@bot.message_handler(regexp=r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    parts = re.match(
        r"^sumar ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    result = oper1 + oper2
    bot.reply_to(
        message,
        f"\U0001F522 Resultado: {result}")

@bot.message_handler(regexp=r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$")
def on_add(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    parts = re.match(
        r"^dividir ([+-]?([0-9]*[.])?[0-9]+) y ([+-]?([0-9]*[.])?[0-9]+)$",
        message.text,
        flags=re.IGNORECASE)
    # print (parts.groups())
    oper1 = float(parts[1])
    oper2 = float(parts[3])
    if oper2 == 0:
        reply(True, message)
    else:
        result = oper1 / oper2
        reply(False, message, result)

def reply(flag, message, result = 0):
    if flag == True:
            return bot.reply_to(message, f"\U0001F522 No se puede dividir por 0")
    else:
            return bot.reply_to(message, f"\U0001F522 Resultado: {result}")   

@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.reply_to(
        message,
        "\U0001F63F Ups, no entendí lo que me dijiste.")

#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################