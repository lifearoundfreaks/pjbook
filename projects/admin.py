from django.contrib import admin
from .models import Category, SubCategory, Project


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('name', 'category', )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('name', 'category', 'subcategory', )
    prepopulated_fields = {"slug": ("name",)}
