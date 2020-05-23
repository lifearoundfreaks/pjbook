from django.urls import path
from .views import ChatView, ChatDetail, ChatCreate, RoomDelete
from .views import MembersRoomView, rooms


urlpatterns = [
    path('', ChatView.as_view(), name='home'),
    path('<int:pk>', ChatDetail.as_view(), name='detail'),
    path('create/', ChatCreate.as_view(), name='create'),
    path('<int:pk>/delete/', RoomDelete.as_view(), name='delete'),
    path('join/', MembersRoomView.as_view(), name='join'),
    path('rooms/', rooms, name='rooms'),
]