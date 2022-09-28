# Generated by Django 4.1.1 on 2022-09-28 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre_cliente', models.CharField(max_length=100)),
                ('apellido_cliente', models.CharField(max_length=100)),
                ('dni_cliente', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('domicilio', models.CharField(max_length=200)),
                ('ciudad_cliente', models.CharField(max_length=100)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('reserva', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Niñera',
            fields=[
                ('nombre_niñera', models.CharField(max_length=100)),
                ('apellido_niñera', models.CharField(max_length=100)),
                ('dni_niñera', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('ciudad_niñera', models.CharField(max_length=100)),
                ('email_niñera', models.EmailField(max_length=254)),
                ('puntaje', models.FloatField()),
                ('precio', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
                ('reserva', models.IntegerField(unique=True)),
                ('fecha_reserva', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
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
