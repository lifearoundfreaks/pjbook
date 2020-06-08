from django.urls import path, include
from django.conf import settings
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    *(path(route, include(f'{app_name}.urls'))
      for app_name, route in getattr(settings, "AUTOROUTED_APPS", {}).items())
]
