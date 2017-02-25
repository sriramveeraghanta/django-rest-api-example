from django.conf.urls import url

from .views import get_auth_token
from rest_framework.authtoken import views as rest_framework_views


urlpatterns = [
    url(r'^login/$', get_auth_token, name='login'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]