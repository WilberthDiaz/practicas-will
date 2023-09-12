from django.db import models
from category.models import Category #Importamls la clase categoria y sus modelos
from django.urls import reverse #Estamos llamando a la urls y devolviendo el reverse


# Create your models here.
class Product(models.Model): #Tabla de requerimientos del producto
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField() #Aqui se ingresa el precio
    images = models.ImageField(upload_to='photos/products')
    stock = models.BooleanField(default=True) #Prodcutos en existencia
    is_available = models.BooleanField(default=True) #Disponible o no 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #Se eliminaran los productos en la categoria correspondiente al eliminarla
    created_date = models.DateTimeField(auto_now_add=True) #Se agregara el valor de la fecha
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug]) #Estaremos generando una URL dinamica, dentro de esta funcion llama a product detail en conjunto slug 
    
    def __str__(self):
        return self.product_name
    
