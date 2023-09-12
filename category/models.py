from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model): #modelo de categorias
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)#Parte final URL
    cat_image = models.ImageField ( upload_to='photos/categories', blank = True)
    
    class Meta: #cambiar nombre en plural
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug]) #Genra el URL dde la base de datos
        
    #Se extraen desde la app store porque estamos trabajando en conjunto con ella
    
    def __str__(self): #mandar a llamar el nombre
        return self.category_name
    
    #Volver a ejecuat el archivo de migracion cuando se generen cambios