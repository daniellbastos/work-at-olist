from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.channels import serializers
from apps.channels.models import Category, Channel


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()

    def get_serializer_class(self):
        pk = self.kwargs.get('pk', None)
        if pk:
            return serializers.ChannelDetailSerializer
        else:
            return serializers.ChannelListSerializer


class CategoryView(GenericViewSet, RetrieveModelMixin):
    serializer_class = serializers.CategoryDetailSerializer
    queryset = Category.objects.all()
