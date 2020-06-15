from django.db import models
from .managers import ProjectManager


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name


class Project(models.Model):
    objects = ProjectManager()

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategories = models.ManyToManyField(Subcategory, blank=True)
    views = models.IntegerField(default=0)

    objects = ProjectManager()

    class Meta:
        verbose_name_plural = "projects"
        ordering = ['-id']

    def __str__(self):
        return self.name
