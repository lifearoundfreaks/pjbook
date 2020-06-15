from django.urls import path, include
from django.conf import settings


urlpatterns = [
    *(path(route, include(f'{app_name}.urls'))
      for app_name, route in getattr(settings, "AUTOROUTED_APPS", {}).items())
]
