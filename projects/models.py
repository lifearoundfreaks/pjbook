from django.db import models
from .manager import ProjectManager


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.CASCADE)
    subcategory = models.ManyToManyField(Subcategory)

    objects = ProjectManager()

    class Meta:
        verbose_name_plural = "projects"

    def __str__(self):
        return self.name
