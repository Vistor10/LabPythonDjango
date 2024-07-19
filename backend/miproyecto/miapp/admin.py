from django.contrib import admin
from .models import Restaurant, Critica, UserProfile
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Critica)
admin.site.register(UserProfile)