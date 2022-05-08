from django.db import models

# Create your models here.

class Alquiler(models.Model):  
    tipo=models.CharField(max_length=50)
    metros=models.IntegerField()
    ambientes=models.CharField(max_length=50)
    antiguedad=models.CharField(max_length=50)
    ubicación=models.CharField(max_length=50)

    def __str__(self):
        return self.tipo+" "+str(self.metros)+" metros cuadrados, "+str(self.ambientes)+" ambientes, "+str(self.antiguedad)+" de antigëdad, "+self.ubicación+" "


class Compra(models.Model):
    tipo=models.CharField(max_length=50)
    metros=models.IntegerField()
    ambientes=models.CharField(max_length=50)
    antiguedad=models.CharField(max_length=50)
    ubicación=models.CharField(max_length=50)

    def __str__(self):
        return self.tipo+" "+str(self.metros)+" metros cuadrados, "+str(self.ambientes)+" ambientes, "+str(self.antiguedad)+" de antigëdad, "+self.ubicación+" "



class Venta(models.Model):
    tipo=models.CharField(max_length=50)
    metros=models.IntegerField()
    ambientes=models.CharField(max_length=50)
    antiguedad=models.CharField(max_length=50)
    ubicación=models.CharField(max_length=50)

    def __str__(self):
        return self.tipo+" "+str(self.metros)+" metros cuadrados, "+str(self.ambientes)+" ambientes, "+str(self.antiguedad)+" de antigëdad, "+self.ubicación+" "




