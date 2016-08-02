import factory

from apps.channels.models import Channel, Category


class ChannelFactory(factory.DjangoModelFactory):
    class Meta:
        model = Channel

    name = factory.Sequence(lambda x: 'Channel #{0}'.format(x))


class CategorylFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda x: 'Category #{0}'.format(x))
