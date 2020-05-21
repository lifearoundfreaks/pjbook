from django.db import models 
from django.contrib.auth.models import User
from .manager import RoomManager, MembersRoomManager, MessageManager
from django.db.models.signals import post_save
from pytils.translit import slugify
import itertools
from django.dispatch import receiver


class Room(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(User, verbose_name="Автор",
                               related_name="author",
                               on_delete=models.CASCADE)
    created_date = models.DateTimeField("Date created", auto_now=True,
                                        auto_now_add=False)
    choice_type = [
        ('private', 'Приватный'),
        ('public', 'Публичный'),
        ('channel', 'Канал'),
    ]
    type_room = models.CharField(max_length=12, choices=choice_type,
                                 default='public')
    slug = models.SlugField(default='')

    objects = RoomManager()

    def __str__(self):
        return self.name

    def _generate_slug(self):
        value = self.name
        slug_candidate = slug_original = slugify(value)
        slug_candidate = slug_candidate.replace('-', '')
        for i in itertools.count(1):
            if not Room.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}{}'.format(slug_original, i)
        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)


class MembersRoom(models.Model):
    room = models.ForeignKey(Room, verbose_name="Chat",
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User",
                             related_name="user", on_delete=models.CASCADE)

    objects = MembersRoomManager()

    def __str__(self):
        return self.room.name


class Message(models.Model):
    sender = models.ForeignKey(User, verbose_name="Отправитель",
                               related_name="sender", on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField("Date created",
                                        auto_now=True, auto_now_add=False)
    room = models.ForeignKey(Room, verbose_name="Chat",
                             on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, verbose_name="Получатель",
                                  null=True, blank=True,
                                  related_name="recipient",
                                  on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    objects = MessageManager()

    def last_30_message(self):
        return Message.objects.order_by('-created_date').all()[:10]


@receiver(signal=post_save, sender=Room)
def post_save_handler(instance, **kwargs):
    user = instance.author
    MembersRoom.objects.create(user=user, room=instance)