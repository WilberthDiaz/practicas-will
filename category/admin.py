from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin): #Automatizacion de categorias llenado automatico
    prepopulated_fields = {'slug': ('category_name',)} #Contenido del SLUG
    list_display = ('category_name', 'slug') #me muestra la lista


admin.site.register(Category, CategoryAdmin)