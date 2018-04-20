import os
import telebot
import requests

bot_api_token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(bot_api_token)

download_root = "https://api.telegram.org/file/bot{token}/".format(token=bot_api_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "I think too that " + message.text)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Cool photo !")
    ph = message.photo[-1]
    fil = bot.get_file(ph.file_id)
    dl_url = download_root + fil.file_path

    photo_data_resp = requests.get(dl_url)

    photo_data_resp.raise_for_status()

    open(os.path.basename(fil.file_path),"wb").write(photo_data_resp.content)


print("Start polling")
bot.polling()
