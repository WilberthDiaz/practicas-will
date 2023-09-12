from django.shortcuts import render, get_object_or_404 
from .models import Product #Mandano a llamar la clase producto del modelo
from category.models import Category

# Create your views here.
def store(request, category_slug=None): #Cuando se agrega NONE es para inicializar
    categories = None #Inicializar
    products = None #Inicalizar
    
    if category_slug != None: #Si la categoria es diferente de NONE va a ser a lo siguiente
        categories = get_object_or_404(Category, slug=category_slug) #Se realiza la comparacion de la categoria, si encuentra la categoria correra y si no lanza el error 404
        products = Product.objects.filter(category=categories, is_available=True) #Filtrando los productos por categoria
        product_count = products.count() #
        
    else: #
        products = Product.objects.all().filter(is_available=True) #Mandando a llamar todos los productos
        product_count = products.count() #Devolver la cantidad de productos que tengo en la base de datos 
    
    context = {
        'products' : products,
        'product_count' : product_count,
    } #Hay que incorporales a un diccionario de esta manera
    
    return render(request, 'store/store.html', context) #Mandando a llamar al html

def product_detail(request, category_slug, product_slug): #Estoy mandando a llamar los productos dentro del slug de categoria
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)#Se hacen dos condiciones (cuando se agregan dos guiones bajos representa que extreaera la info)
    except Exception as e: #Si lo primero no ocurre arrojara una excepcion 
        raise e
    
    context = {
        'single_product': single_product #La variabe se asignara dentro del diccionario 
    }
    
        
    return render(request, 'store/product_detail.html', context) #Mando a llamar el producto en su HTML