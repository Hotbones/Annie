from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Niñera(models.Model):
    
    perfil = models.OneToOneField(User, on_delete=models.CASCADE)

    TURNOS = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]
    turnos = MultiSelectField(choices=TURNOS,max_length=50,null=True, blank=True)

    HABILIDADES = [
        ('Cocina', 'Cocina'),
        ('Maneja', 'Maneja'),
        ('Limpieza', 'Limpieza'),
        ('Traslado', 'Traslado'),
    ]
    habilidades = MultiSelectField(choices=HABILIDADES,max_length=50,null=True, blank=True)

    EDADES = [
        ('0 - 3 años', '0 - 3 años'),
        ('4 - 6 años', '4 - 6 años'),
        ('7 - 10 años', '7 - 10 años'),
        ('11 - 13 años', '11 - 13 años'),
    ]
    edades = MultiSelectField(choices=EDADES,max_length=80,null=True, blank=True)

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True, error_messages ={"unique":"Este DNI ya está registrado."},null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True, default='1990-10-10')
    ciudad = models.CharField(max_length=100,null=True, blank=True)
    telefono = models.CharField(max_length=10, help_text='Número sin 0 ni 15',null=True, blank=True)
    tarifa_por_hora = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    foto_perfil = models.ImageField(upload_to='img_niñeras/', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Niñera'
        verbose_name_plural = 'Niñeras'
    
    def __str__(self):
        return self.nombre


class Cliente(models.Model):

    perfil = models.OneToOneField(User, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    dni = models.IntegerField(unique=True, error_messages ={"unique":"Este DNI ya está registrado."})
    domicilio = models.CharField(max_length=200,null=True, blank=True)
    ciudad = models.CharField(max_length=100,null=True, blank=True)
    telefono = models.CharField(max_length=10,help_text='Número sin 0 ni 15',null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)


    
    foto_perfil = models.ImageField(upload_to='img_clientes/', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nombre




class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    comentarista = models.CharField(max_length=200)
    puntaje = models.FloatField(default=0) # estrellas??
    mensaje = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.mensaje[0:50]

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    niñera = models.ForeignKey(Niñera, on_delete=models.CASCADE)

    fecha = models.DateTimeField()
    hora = models.IntegerField()
    lugar = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.cliente} Hizo una reserva a {self.niñera}'