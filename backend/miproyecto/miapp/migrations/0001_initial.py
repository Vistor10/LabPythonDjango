# Generated by Django 5.0.6 on 2024-06-14 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Codigo', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Critica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Opinion', models.CharField(max_length=500)),
                ('calificacion', models.IntegerField(choices=[('1', '1 estrella'), ('2', '2 estrellas'), ('3', '3 estrellas'), ('4', '4 estrellas'), ('5', '5 estrellas')])),
                ('Critico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Nombre_Restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.restaurant')),
            ],
        ),
    ]
