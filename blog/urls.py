from django.conf.urls import include, url
from rest_framework import routers
from .views import PostAPIView

router = routers.DefaultRouter()
router.register(r'posts', PostAPIView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
