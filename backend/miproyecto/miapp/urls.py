from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, CriticaViewSet, UserViewSet, restaurant_list_view, register, home, login_view, restaurant_cabrera, restaurant_zanzibar, restaurant_capogrossi, restaurant_borago, restaurant_AmbrosiaBistro, restaurant_DivertimentoChileno, Suscripcion, SuscripcionSucces, PasswordRefresh

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'criticas', CriticaViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('restaurants/', restaurant_list_view, name='restaurant-list'),
    path('registrochef/', register, name='registrochef'),
    path('paginalogin/', login_view, name='paginalogin'),
    path('paginarestaurant/', restaurant_cabrera, name='paginarestaurant'),
    path('paginarestaurant1/', restaurant_zanzibar, name='paginarestaurant1'),
    path('paginarestaurant2/', restaurant_capogrossi, name='paginarestaurant2'),
    path('paginarestaurant3/', restaurant_borago, name='paginarestaurant3'),
    path('paginarestaurant4/', restaurant_AmbrosiaBistro, name='paginarestaurant4'),
    path('paginarestaurant5/', restaurant_DivertimentoChileno, name='paginarestaurant5'),
    path('suscripcion/', Suscripcion, name='suscripcion'),
    path('suscripcionrealizada/', SuscripcionSucces, name='suscripcionrealizada'),
    path('recuperarpassword/', PasswordRefresh, name='recuperarpassword')
]
