from django.urls import path
from AppInmo import views
from .views import *

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('alquiler', views.alquiler,name="alquiler"),
    path('compra', views.compra, name="compra"),
    path('venta', views.venta, name="venta"),

    path('formulario', views.alquilerFormulario, name="alquilerformulario"),
]
