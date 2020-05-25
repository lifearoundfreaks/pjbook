from django.utils.text import slugify
from django.db.models.signals import pre_save
from .models import Category, Subcategory, Project


def category_pre_save_listener(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


def subcategory_pre_save_listener(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


def project_pre_save_listener(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(category_pre_save_listener, sender=Category)
pre_save.connect(subcategory_pre_save_listener, sender=Subcategory)
pre_save.connect(project_pre_save_listener, sender=Project)
