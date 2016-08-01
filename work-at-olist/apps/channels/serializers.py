from rest_framework import serializers

from apps.channels.models import Category, Channel


class ChannelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name')


class ChannelDetailSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Channel
        fields = ('id', 'name', 'categories')

    def get_categories(self, obj):
        return obj.categories.filter(parent__isnull=True).values('id', 'name')


class CategoryDetailSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children')

    def get_parent(self, obj):
        if obj.parent:
            return {'id': obj.parent.pk, 'name': obj.parent.name}
        return {}

    def get_children(self, obj):
        return obj.children.all().values('id', 'name')
