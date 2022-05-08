
from django.contrib import admin

from ProyectoCoderInmo.views import saludo
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('AppInmo/', include('AppInmo.urls')),
]
