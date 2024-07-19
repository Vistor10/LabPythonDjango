from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#class UserProfile(models.Model):
   #user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
   #name = models.CharField(max_length=30, blank=True, null=True)
   #role = models.CharField(max_length=30, blank=True, null=True)
   #email = models.CharField(max_length=20, blank=True, null=True)
   #password1 = models.CharField(max_length=50, blank=True, null=True)
   #date = models.DateField(blank=True, null=True)
   #photo = models.ImageField(upload_to='certificados/', blank=True, null=True)

   #def __str__(self):
   #    return self.user.username
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    photo = models.FileField(upload_to='certificados/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Restaurant(models.Model): 
    Codigo=models.CharField(max_length=20, primary_key=True, unique=True)
    Nombre= models.CharField(max_length=100)
    Direccion=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Codigo} : {self.Nombre} : {self.Direccion}"

class Critica(models.Model):
    Critico=models.ForeignKey(User, on_delete=models.CASCADE)
    Opinion= models.CharField(max_length=500)
    Nombre_Restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    CALIFICACION=[
        ('1', '1 estrella'),
        ('2', '2 estrellas'),
        ('3', '3 estrellas'),
        ('4', '4 estrellas'),
        ('5', '5 estrellas'),
    ]
    calificacion=models.IntegerField(choices=CALIFICACION)
    def __str__(self):
        return f"{self.Critico} : {self.Opinion} : {self.Nombre_Restaurant}"
