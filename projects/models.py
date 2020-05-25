from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from .manager import Manager


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    objects = Manager()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = Manager()

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.CASCADE)
    subcategory = models.ManyToManyField(Subcategory)

    objects = Manager()

    class Meta:
        verbose_name_plural = "projects"

    def __str__(self):
        return self.name


def save_slug_category(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


def save_slug_subcategory(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


def save_slug_project(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(save_slug_category, sender=Category)
pre_save.connect(save_slug_subcategory, sender=Subcategory)
pre_save.connect(save_slug_project, sender=Project)
