from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"), #nombre de la funcion y lo siguiente es programar la funcion
    path('category/<slug:category_slug>/', views.store, name='products_by_category'), #Funcion para procesar los pedidos siguiente paso modificar el views
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), #Con esta funcion nos abrira la segunda pagina donde podemos ver el producto
    path('search/', views.search, name='search'),#Estamos definiendo un path donde estamos utlizando en motor de busqueda en la aplicacion
  ]


#Esta carpeta se creo manualmente para la seccion de URLS, para todo articulo que se trabajara en la seccion de tienda