from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('apps.channels.urls')),
    url(r'^admin/', admin.site.urls),
]
