from rest_framework import serializers
from .models import Restaurant, Critica
from django.contrib.auth.models import User


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields="__all__"

class CriticaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Critica
        fields="__all__" 

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Restaurant, Critica

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role', 'fecha_nacimiento', 'certificado']

class UserSerializers(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'userprofile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile')
        profile = instance.userprofile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        profile.role = profile_data.get('role', profile.role)
        profile.fecha_nacimiento = profile_data.get('fecha_nacimiento', profile.fecha_nacimiento)
        profile.certificado = profile_data.get('certificado', profile.certificado)
        profile.save()

        return instance
    