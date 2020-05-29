from .models import Project, SubCategory, Category
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


class ProjectView(TemplateView):

    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["subcategories"] = SubCategory.objects.all() 
        return context


class DetailCategory(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subcategories"] = SubCategory.objects.filter(
                                    category__id=self.get_object().id)
        return context
