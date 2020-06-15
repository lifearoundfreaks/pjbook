from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pjbook_theme/home.html'
