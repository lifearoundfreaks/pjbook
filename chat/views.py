from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView
from django.views.generic import DeleteView
from .models import Room, Message, MembersRoom
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View


class ChatView(TemplateView):

    template_name = 'chat/chat_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session.get('_auth_user_id')
        context["title"] = "Главная"
        context["rooms"] = Room.objects.get_public()
        context["now"] = timezone.now()
        context["id_user"] = id
        return context


class ChatDetail(DetailView):

    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        id = self.request.session.get('_auth_user_id')
        user = User.objects.get(id=id)
        is_member = MembersRoom.objects.get_member_room(user, obj)
        context['messages'] = Message.objects.all().filter(room=obj)
        context['now'] = timezone.now()
        context["rooms"] = Room.objects.get_public()
        context["id_user"] = id
        context['is_member'] = is_member
        context['title'] = obj.name
        return context


class ChatCreate(CreateView):
    model = Room
    fields = ('name', 'type_room')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session.get('_auth_user_id')
        context["rooms"] = Room.objects.get_public()
        context["now"] = timezone.now()
        context["id_user"] = id
        return context

    def form_valid(self, form, **kwargs):
        id = self.request.session.get('_auth_user_id')
        if form.is_valid():
            form.instance.author = User.objects.get(id=id)
            self.object = form.save()
            return redirect('chat')


def rooms(request):
    typ = request.GET.get('type')
    id = request.session.get('_auth_user_id')
    context = {}
    context["now"] = timezone.now()
    context["id_user"] = id
    if typ == 'all':
        context["rooms"] = Room.objects.get_public()
    else:
        context["rooms"] = Room.objects.filter(author=User.objects.get(id=id))

    return render(request, "chat/chat_list.html", context)


class MembersRoomView(View):

    def get(self, request, *args, **kwargs):
        slug = request.GET.get('slug')
        id = self.request.session.get('_auth_user_id') 
        room = Room.objects.get_by_slug(slug)[0] 
        user = User.objects.get(id=id)
        context = {}
        is_member = MembersRoom.objects.get_member_room(user, room)
        if not is_member:
            MembersRoom.objects.create(user=user, room=room)
            is_member = True
        context['now'] = timezone.now()
        context["rooms"] = Room.objects.get_public()
        context['messages'] = Message.objects.all().filter(room=room)
        context["id_user"] = id
        context['object'] = room
        context['is_member'] = is_member

        return render(request, "chat/room_detail.html", context)


class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('chat')
