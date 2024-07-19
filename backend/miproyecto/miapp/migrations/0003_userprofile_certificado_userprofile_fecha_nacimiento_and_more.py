# Generated by Django 5.0.6 on 2024-07-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='certificado',
            field=models.FileField(blank=True, null=True, upload_to='certificados/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('usuario', 'Usuario'), ('critico', 'Critico'), ('dueño', 'Dueño')], default='usuario', max_length=30),
        ),
    ]