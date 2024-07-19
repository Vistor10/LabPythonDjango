from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Restaurant, Critica, UserProfile
from django.contrib.auth.models import User
from .serializers import RestaurantSerializer, CriticaSerializer, UserSerializers
from django.contrib import messages
from .forms import UserRegisterForm 
from django.contrib.auth.decorators import login_required

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CriticaViewSet(viewsets.ModelViewSet):
    queryset = Critica.objects.all()
    serializer_class = CriticaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


@login_required
def home(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    user_role = user_profile.role if user_profile else None
    return render(request, 'paginainicio.html', {'user_role': user_role})

def restaurant_list_view(request):
    return render(request, 'forochef.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear el usuario en el modelo User de Django
            user = form.save(commit=False)  # No guarda aún el User, necesitamos primero asignar el email y la contraseña
            user.email = form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            
            # Crear el perfil de usuario
            role = form.cleaned_data.get('rol')
            date = form.cleaned_data.get('fecha_nacimiento')
            photo = form.cleaned_data.get('certificado')
            user_profile = UserProfile(user=user, role=role, date=date, photo=photo)
            user_profile.save()
            
            messages.success(request, f'Cuenta creada para {user.username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registrochef.html', {'form': form})

def login_view(request):
    return render(request, 'paginalogin.html')

def restaurant_cabrera(request):
    return render(request, 'paginarestaurant.html')

def restaurant_zanzibar(request):
    return render(request, 'paginarestaurant1.html')

def restaurant_capogrossi(request):
    return render(request, 'paginarestaurant2.html')

def restaurant_borago(request):
    return render(request, 'paginarestaurant3.html')

def restaurant_AmbrosiaBistro(request):
    return render(request, 'paginarestaurant4.html')

def restaurant_DivertimentoChileno(request):
    return render(request, 'paginarestaurant5.html')

def Suscripcion(request):
    return render(request, 'suscripcion.html')

def SuscripcionSucces(request):
    return render(request, 'suscripcionrealizada.html')

def PasswordRefresh(request):
    return render(request, 'recuperarpassword.html')