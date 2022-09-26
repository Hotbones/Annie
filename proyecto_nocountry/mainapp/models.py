from django.db import models

class Niñera(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100)
    puntaje = models.FloatField()

    class Meta:
        verbose_name = 'Niñera'
        verbose_name_plural = 'Niñeras'
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    pass