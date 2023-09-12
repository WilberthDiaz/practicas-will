from django.shortcuts import render
from store.models import Product #Importancion de la tienda de productos 


def home(request):
    products = Product.objects.all().filter(is_available=True) #Extrayendo todos los productos y filtralos por su disposicion 
    
    
    context = {
        'products': products,          #envolviendo en un diccionario
    }
    
    return render(request, 'home.html', context) #Mandando a llamar los valores y se envien a la pagina