from django.db import models
from django.contrib.auth.models import User

class Niñera(models.Model):
    nombre_niñera = models.CharField(max_length=100)
    apellido_niñera = models.CharField(max_length=100)
    dni_niñera = models.IntegerField(unique=True, primary_key=True)
    fecha_nacimiento = models.DateField()
    ciudad_niñera = models.CharField(max_length=100)
    email_niñera = models.EmailField()
    puntaje = models.FloatField()
    precio = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # verificacion [activo,foto_cargada,anteced_penales]

    class Meta:
        verbose_name = 'Niñera'
        verbose_name_plural = 'Niñeras'
    
    def __str__(self):
        return self.nombre_niñera

class Cliente(models.Model):

    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    dni_cliente = models.IntegerField(unique=True, primary_key=True)
    domicilio = models.CharField(max_length=200)
    ciudad_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    reserva = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nombre_cliente


class Reserva(models.Model):
    reserva = models.IntegerField(unique=True)
    # view que crea reserva y asignarlo a cliente y niñera
    fecha_reserva = models.DateField() # 2022-09-28
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
    def __str__(self):
        return str(self.reserva)

class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.mensaje[0:50]
