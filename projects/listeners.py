from .models import Category, Project, Subcategory
from django.utils.text import slugify
from django.db.models.signals import pre_save


def project_pre_save_category(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


def project_pre_save_subcategory(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


def project_pre_save_listener(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(project_pre_save_category, sender=Category)
pre_save.connect(project_pre_save_subcategory, sender=Subcategory)
pre_save.connect(project_pre_save_listener, sender=Project)
