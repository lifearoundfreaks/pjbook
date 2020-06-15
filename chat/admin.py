from django.contrib import admin
from .models import Room, MembersRoom, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_date', 'type_room', 'slug', )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MembersRoom)
class MembersRoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'sender', 'recipient', 'text', 'created_date', )
