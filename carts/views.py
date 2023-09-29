from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product #Importando el producto
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist #Exportamos la excepcion 


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

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request)) #Instanciamos cart, el cart id busca el valor de en la funcion _cart_id que se creo
    product = get_object_or_404(Product, id=product_id) #Llamamos al objeto, nos llama lo que queremos buscar en dos parametros, mandamos a llamar la tabla y al objeto en la tabla  
    cart_item = CartItem.objects.get(product=product, cart=cart)
    
    if cart_item.quantity>1: #Si la cantidad de elementos es mayor a 1 hay que decrecer
        cart_item.quantity -=1 #Se disminuira en 1 la cantidad
        cart_item.save() # 
        
    else:
        cart_item.delete() #Si es menor que 0 se elimina
        
    return redirect('cart') #Me redirecciona a la pagina Cart

def remove_cart_item(request, product_id):#Eliminara el producto si llega a 0
    cart =Cart.objects.get(cart_id=_cart_id(request)) #Busque el objeto
    product = get_object_or_404(Product, id=product_id) #Obtener el objeto llamando la identidad esta buscando el parametro
    cart_item = CartItem.objects.get(product=product, cart=cart) #Buscando por el producto 
    cart_item.delete()
    return redirect('cart') #Redireccionamos al cart
#Realizando esto tenemos que registrar el path
    

def cart(request, total=0, quantity=0, cart_items=None ): #Extrayendo la solicitud, 
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) 
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2*total)/100
        grand_total = total + tax
            
    except ObjectDoesNotExist:
        pass #Ignorara toda la excepcion 
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }
              
    return render(request, 'store/cart.html', context) #Solicitud se extrae de store porque es la pagina principal de la tienda