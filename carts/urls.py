from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'), #Creando el archivo path (comillas en blanco para ingresar los datos,seleccionar el views cart, nombre de la funcion)
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
]
