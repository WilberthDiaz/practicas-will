from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'), #Creando el archivo path (comillas en blanco para ingresar los datos,seleccionar el views cart, nombre de la funcion)
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'), #Dar de alta la funcion que agrega productos
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'), #Dar de alta la funcion que elimina en el cart
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]
