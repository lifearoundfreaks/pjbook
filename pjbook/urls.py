from django.contrib import admin
from django.urls import path, include
from .view import BaseView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='home'),
    path('account/', include('accounts.urls'))
]
