from django.urls import path
from .views import ChatView, ChatDetail, ChatCreate, RoomDelete
from .views import MembersRoomView, rooms


urlpatterns = [
    path('', ChatView.as_view(), name='home'),
    path('chats/<int:pk>', ChatDetail.as_view(), name='detail'),
    path('chats/create/', ChatCreate.as_view(), name='create'),
    path('chats/<int:pk>/delete/', RoomDelete.as_view(), name='delete'),
    path('chats/join/', MembersRoomView.as_view(), name='join'),
    path('rooms/', rooms, name='rooms'),
]