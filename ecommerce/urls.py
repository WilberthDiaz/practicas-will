"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #Se importan palabras claves si estamos trabajando con paht
from . import views
from django.conf.urls.static import static  #IMPORTACION DE ELEMENTOS QUE SE REQUIERAN
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('store/', include('store.urls')), #Creando la pagina de store
    path('cart/', include ('carts.urls')), #Creando la pagina del carrito de compras #Ojo con los parentesis
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Documentacion de configuraciones
