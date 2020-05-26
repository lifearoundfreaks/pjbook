from django.db import models
from django.db.models import Q


class RoomQuerySet(models.QuerySet):

    def get_public(self):
        return self.filter(type_room='public')

    def get_by_slug(self, slug):
        return self.filter(slug=slug)


class RoomManager(models.Manager):

    def queryset(self):
        return RoomQuerySet(self.model, using=self._db)

    def get_public(self):
        return self.queryset().get_public()

    def get_by_slug(self, slug):
        return self.queryset().get_by_slug(slug)


class MembersRoomQuerySet(models.QuerySet):

    def get_member_room(self, user, room):
        obj = self.filter(user=user, room=room)
        if obj.exists():
            return True
        return False


class MembersRoomManager(models.Manager):

    def queryset(self):
        return MembersRoomQuerySet(self.model, using=self._db)

    def get_member_room(self, user, room):
        return self.queryset().get_member_room(user, room)


class MessagesQuerySet(models.QuerySet):

    def count_unread_messages_for_user(self, room_id, id_user):
        return self.filter(~Q(user_id=id_user),
                            room__id=room_id, read=False).count()

    def filter_by_id(self, msg_id):
        return self.filter(id=msg_id)


class MessageManager(models.Manager):

    def queryset(self):
        return MessagesQuerySet(self.model, using=self._db)

    def count_unread_messages_for_user(self, room_id, id_user):
        return self.queryset().count_unread_messages_for_user(room_id, id_user)

    def filter_by_id(self, msg_id):
        return self.queryset().filter_by_id(msg_id)
