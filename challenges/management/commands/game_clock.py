import sys
import time

from django.core.management.base import BaseCommand, CommandError
from challenges import services

class Command(BaseCommand):
    help = 'Game clock'

    def add_arguments(self, parser):
        parser.add_argument('run_interval', type=int)
        # pass

    def handle(self, *args, **options):
        sleep_time = options['run_interval']

        while True:
            print('Updating score')

            services.update_monster_score(-1)

            print('Sleeping for {}s'.format(sleep_time))

            time.sleep(sleep_time)