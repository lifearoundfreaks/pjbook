from django.urls import path
from .views import CategoryView, ProjectView, PopularProjectsView


urlpatterns = [
    path('', PopularProjectsView.as_view(), name='popular_projects'),
    path('categories/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('projects/<slug:slug>/', ProjectView.as_view(), name='project'),
]
