from django.shortcuts import render
from .models import Project, SubCategory, Category


def my_view(request):
    context = {
        'categories': Category.objects.all(),
        'subcategories': SubCategory.objects.all(),
        'projects': Project.objects.all()
    }
    return render(request, '', context=context)


def filter_category(request, category_id):
    context = {
        'categories': Category.objects.all(),
        'subcategories': SubCategory.objects.all(),
        'projects': Project.objects.get_category_id(category_id)
    }
    return render(request, '', context=context)
