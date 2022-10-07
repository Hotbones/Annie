# Generated by Django 4.1.1 on 2022-10-05 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.IntegerField(error_messages={'unique': 'Este DNI ya está registrado.'}, primary_key=True, serialize=False, unique=True)),
                ('domicilio', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(help_text='Número sin 0 ni 15', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('perfil_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Niñera',
            fields=[
                ('turnos', multiselectfield.db.fields.MultiSelectField(choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], max_length=50)),
                ('habilidades', multiselectfield.db.fields.MultiSelectField(choices=[('Cocina', 'Cocina'), ('Maneja', 'Maneja'), ('Limpieza', 'Limpieza'), ('Traslado', 'Traslado')], max_length=50)),
                ('edades', multiselectfield.db.fields.MultiSelectField(choices=[('0 - 3 años', '0 - 3 años'), ('4 - 6 años', '4 - 6 años'), ('7 - 10 años', '7 - 10 años'), ('11 - 13 años', '11 - 13 años')], max_length=80)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.IntegerField(error_messages={'unique': 'Este DNI ya está registrado.'}, primary_key=True, serialize=False, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('ciudad', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(help_text='Número sin 0 ni 15', max_length=10)),
                ('tarifa_por_hora', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('perfil_niñera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Niñera',
                'verbose_name_plural': 'Niñeras',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cliente')),
                ('niñera_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.niñera')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.FloatField(default=0)),
                ('mensaje', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
    ]
