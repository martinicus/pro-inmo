from django.contrib import admin
from .models import Alquiler,Venta,Compra

# Register your models here.
admin.site.register(Compra)

admin.site.register(Venta)

admin.site.register(Alquiler)
