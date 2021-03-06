import apiai
import json


def textMessage(s):
    request = apiai.ApiAI('3c95cc79f20a4b8eadf4178ee3ecbf14').text_request()
    request.lang = 'ru'
    request.session_id = 'any_session_id'
    request.query = s
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        return response


import telebot

telebot.apihelper.proxies = {'https': 'socks5h://216.144.230.233:15993'}
TG_TOKEN = "1243964521:AAFTqJlCx1pNIBMYDc7gmlq1-A9lbjj-Ljg"

bot = telebot.TeleBot(TG_TOKEN)
bot.remove_webhook()


@bot.message_handler(content_types=['text'])
def handle_text(message):
    # TODO conditions for processing string from textMessage(message.text)
    bot.send_message(message.chat.id, textMessage(message.text))


bot.polling()
