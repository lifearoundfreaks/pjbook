from django.urls import path
from .views import DetailCategory, ProjectView


urlpatterns = [
    path('', ProjectView.as_view(), name='home'),
    path('projects/<int:pk>', DetailCategory.as_view(), name='detail_category')
]
