from rest_framework import routers

from apps.channels.views import ChannelViewSet, CategoryView


router = routers.DefaultRouter()
router.register(r'channel', ChannelViewSet)
router.register(r'category', CategoryView)


urlpatterns = router.urls
