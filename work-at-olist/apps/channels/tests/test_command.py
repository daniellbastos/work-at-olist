from django.conf import settings
from django.core import management
from django.test import TestCase

from apps.channels.models import Channel, Category


class CommandTest(TestCase):
    def setUp(self):
        self.path = settings.FIXTURES_DIRS[0]

    def test_importcategories(self):
        categories_csv = '{0}/categories.csv'.format(self.path)
        management.call_command('importcategories', 'walmart', categories_csv)
        self.assertEquals(Channel.objects.all().count(), 1)
        self.assertEquals(Category.objects.all().count(), 24)
