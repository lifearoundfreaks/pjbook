from django import template
from ..models import Message

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)


@register.simple_tag
def count_msg(room_id, id):
    count = Message.objects.get_count(room_id, id)
    return str(count)


@register.simple_tag
def read_msg(msg_id):
    Message.objects.read_msg(msg_id)