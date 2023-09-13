from django.shortcuts import render, redirect
from store.models import Product #Importando el producto
from .models import Cart, CartItem


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        
    cart.save() #Guardar dentro de la base de datos
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1 #Cuando agregues al carrito se generara un mas 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
        product = product,
        quantity = 1,
        cart = cart,
    )
    cart_item.save()
    return redirect('cart')

    

def cart(request): #Extrayendo la solicitud
    return render(request, 'store/cart.html') #Solicitud se extrae de store porque es la pagina principal de la tienda