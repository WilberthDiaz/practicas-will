from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model): #sIempre se comienza con una class
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True) #Agregando la fecha automatico
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #Representa el producto seleccionado para la compra, se relaciona con la entidad producto y a la vez se elimina por completo 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #Se elimina del carro
    quantity = models.IntegerField() #Se elimina la cantidad el precio y como es diferente las comillas quedan vacias
    is_active = models.BooleanField(default=True) #Si esta activo o nel
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __unicode__(self):
        return self.product #Imprime producto
    
    #Registrar las class en cart
    