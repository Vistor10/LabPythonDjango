from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Critica, Restaurant

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(required=False)
    certificado = forms.FileField(required=False)
    rol = forms.ChoiceField(choices=[('usuario', 'Usuario'), ('critico', 'Crítico'), ('dueño', 'Dueño de Restaurante')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'fecha_nacimiento', 'certificado', 'rol']
