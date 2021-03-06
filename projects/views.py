from django.views.generic import ListView, TemplateView
from .models import Project, Category, Subcategory
from django.db.models import Q


class ProjectView(TemplateView):
    template_name = 'projects/project.html'

    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs.get('slug'))
        project.views += 1
        project.save()
        return {**super().get_context_data(**kwargs), 'project': project}


class ProjectListView(ListView):
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.all()


class PopularProjectsView(ProjectListView):
    template_name = 'projects/popular.html'

    def get_queryset(self):
        return super().get_queryset().order_by('-views', '-id')


class CategoryView(ProjectListView):
    template_name = 'projects/category.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            category__slug=self.kwargs['slug'])

        if 'all_subs' in self.request.POST:
            return queryset.with_all_subcategories(
                self.request.POST.getlist('sub_slug'))
        elif 'sub_slug' in self.request.POST:
            return queryset.with_subcategories(
                self.request.POST.getlist('sub_slug'))

        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        slug = self.kwargs.get('slug')
        return super().get_context_data(
            *args, category=Category.objects.get(slug=slug),
            subcategories=Subcategory.objects.filter(category__slug=slug),
            **kwargs)


class SiteSeachView(ProjectListView):
    template_name = 'projects/search_results.html'

    def get_queryset(self):
        search_term = self.request.GET.get('term', '')
        return super().get_queryset().filter(
            Q(name__contains=search_term) |
            Q(description__contains=search_term))
