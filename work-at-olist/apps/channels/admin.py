from django.contrib import admin

from apps.channels import models


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'channel']


admin.site.register(models.Channel, ChannelAdmin)
admin.site.register(models.Category, CategoryAdmin)
