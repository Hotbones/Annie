from django.db import models
from django.contrib.auth.models import User, AbstractUser
from multiselectfield import MultiSelectField


class Niñera(models.Model):
    
    perfil_niñera = models.OneToOneField(User, on_delete=models.CASCADE)

    TURNOS = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]
    turnos = MultiSelectField(choices=TURNOS,max_length=50)

    HABILIDADES = [
        ('Cocina', 'Cocina'),
        ('Maneja', 'Maneja'),
        ('Limpieza', 'Limpieza'),
        ('Traslado', 'Traslado'),
    ]
    habilidades = MultiSelectField(choices=HABILIDADES,max_length=50)

    EDADES = [
        ('0 - 3 años', '0 - 3 años'),
        ('4 - 6 años', '4 - 6 años'),
        ('7 - 10 años', '7 - 10 años'),
        ('11 - 13 años', '11 - 13 años'),
    ]
    edades = MultiSelectField(choices=EDADES,max_length=80)

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True, primary_key=True,
        error_messages ={
                        "unique":"Este DNI ya está registrado."
                        })
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10, help_text='Número sin 0 ni 15')
    tarifa_por_hora = models.IntegerField()
    descripcion = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # verificacion [activo,foto_cargada,anteced_penales]

    class Meta:
        verbose_name = 'Niñera'
        verbose_name_plural = 'Niñeras'
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):

    perfil_cliente = models.OneToOneField(User, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True,
        error_messages ={
                        "unique":"Este DNI ya está registrado."
                        })
    domicilio = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10,help_text='Número sin 0 ni 15')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    niñera_id = models.ForeignKey(Niñera, on_delete=models.CASCADE)
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
    puntaje = models.FloatField(default=0) # estrellas??
    mensaje = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
    
    def __str__(self):
        return self.mensaje[0:50]
