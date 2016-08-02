from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.channels import factories


class ChannelAPITest(APITestCase):
    def setUp(self):
        self.channel = factories.ChannelFactory()
        self.categories = factories.CategorylFactory.create_batch(
            channel=self.channel, size=5)

        self.channel_list_url = reverse('channel-list')
        self.channel_detail_url = reverse(
            'channel-detail', args=[str(self.channel.pk)])

    def test_channel_list(self):
        response = self.client.get(self.channel_list_url, format='json')

        self.assertEquals(len(response.data), 1)
        self.assertEquals(response.data[0]['name'], self.channel.name)

    def test_channel_detail(self):
        response = self.client.get(self.channel_detail_url, format='json')
        self.assertEquals(response.data['name'], self.channel.name)
        self.assertEquals(len(response.data['categories']), 5)


class CategoriesAPITest(APITestCase):
    def setUp(self):
        self.channel = factories.ChannelFactory()
        self.root = factories.CategorylFactory(channel=self.channel)
        self.node = factories.CategorylFactory(
            channel=self.channel, parent=self.root)
        self.leaf = factories.CategorylFactory(
            channel=self.channel, parent=self.node)

    def test_category_root(self):
        url = reverse('category-detail', args=[str(self.root.pk)])
        response = self.client.get(url, format='json')
        self.assertFalse(response.data['parent'])
        self.assertEquals(len(response.data['children']), 1)

    def test_category_node(self):
        url = reverse('category-detail', args=[str(self.node.pk)])
        response = self.client.get(url, format='json')
        self.assertEquals(response.data['parent']['id'], self.root.pk)
        self.assertEquals(response.data['parent']['name'], self.root.name)
        self.assertEquals(len(response.data['children']), 1)

    def test_category_leaf(self):
        url = reverse('category-detail', args=[str(self.leaf.pk)])
        response = self.client.get(url, format='json')
        self.assertEquals(response.data['parent']['id'], self.node.pk)
        self.assertEquals(response.data['parent']['name'], self.node.name)
        self.assertEquals(len(response.data['children']), 0)
