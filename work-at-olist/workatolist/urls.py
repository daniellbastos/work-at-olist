from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='channels/home.html')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('apps.channels.urls')),
    url(r'^admin/', admin.site.urls),
]
