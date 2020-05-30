from django.urls import path
from .views import DetailCategory, ProjectView


urlpatterns = [
    path('projects/<slug>', DetailCategory.as_view(), name='detail_category')
]
