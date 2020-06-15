from django.contrib import admin
from .models import Category, Subcategory, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('name', 'category', )
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('name', 'category', 'subcategories', )
    prepopulated_fields = {"slug": ("name",)}
