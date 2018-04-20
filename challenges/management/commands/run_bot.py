import os
import telebot
import requests


from django.core.management.base import BaseCommand, CommandError
from clarifai.rest import ClarifaiApp

from challenges.models import Challenge

bot_api_token = os.environ['BOT_API_TOKEN']
bot = telebot.TeleBot(bot_api_token)

download_root = "https://api.telegram.org/file/bot{token}/".format(token=bot_api_token)

current_challenge = None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")

@bot.message_handler(commands=['new'])
def new_challenge(message):
    global current_challenge
    current_challenge = Challenge.objects.order_by('?').first()
    bot.reply_to(message, current_challenge.riddle_text)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global current_challenge
    bot.reply_to(message, "Cool photo !")
    if current_challenge is None:
        bot.reply_to(message, "No challenge running. Run the /new to start a new challenge")
        return

    ph = message.photo[-1]
    fil = bot.get_file(ph.file_id)
    dl_url = download_root + fil.file_path

    response = current_challenge.solve(dl_url)
    if response['valid']:
        bot.reply_to(message, "GG WP!")
        current_challenge = Challenge.objects.order_by('?').first()
        bot.reply_to(message, current_challenge.riddle_text)
        return

    result_message = "That's not what I asked, i only see "

    for prediction in response['guessed']['concepts']:
        result_message += prediction['name'] + ", "

    bot.reply_to(message, result_message)



class Command(BaseCommand):
    help = 'Run the Telegram bot'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print("Start polling")
        bot.polling()

        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
