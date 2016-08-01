import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Channel(BaseModel):
    name = models.CharField('Nome', max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField('Nome', max_length=200)
    parent = models.ForeignKey(
        'self', related_name='children', blank=True, null=True)
    channel = models.ForeignKey(Channel, related_name='categories')

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name
