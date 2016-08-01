import csv

from django.core.management.base import BaseCommand

from apps.channels.models import Category, Channel


class Command(BaseCommand):
    help = 'Import all categories of the CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('channel', type=str)
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        print('Import all categories...')
        channel_name = options['channel']
        print('Channel name: {0}'.format(channel_name))
        self.channel, created = Channel.objects.get_or_create(name=channel_name)
        with open(options['csv_file']) as csv_file:
            self.create_categories(csv_file)

    def create_categories(self, csv_file):
        for row in csv.DictReader(csv_file):
            print('\nCategories: {0}'.format(row['Category']))
            categories_name = row['Category'].split(' / ')
            parent = None
            for name in categories_name:
                category, created = Category.objects.get_or_create(
                    name=name, channel=self.channel, parent=parent)

                if created:
                    print(' - Created: {0}'.format(category))
                parent = category
