from django.urls import re_path
from .consumers import ChatroomConsumer

websocket_urlpatterns = [
    # Matches URLs like /ws/chatroom/public-chat/ or /ws/chatroom/room-1/
    re_path(r'^ws/chatroom/(?P<chatroom_name>[\w-]+)/$', ChatroomConsumer.as_asgi()),
]
