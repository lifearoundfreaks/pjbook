from django.urls import re_path
from django.conf.urls import url

from .consumers import ChatConsumer

websocket_urlpatterns = [
    url(r'/ws/(?P<room_name>\w+)/$', ChatConsumer),
]
