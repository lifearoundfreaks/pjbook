from django.urls import path
from .views import (
    CategoryView, ProjectView, PopularProjectsView, SiteSeachView
)

urlpatterns = [
    path('', PopularProjectsView.as_view(), name='popular_projects'),
    path('categories/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('projects/<slug:slug>/', ProjectView.as_view(), name='project'),
    path('projects/search', SiteSeachView.as_view(), name='search'),
]
