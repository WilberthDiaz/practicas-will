from .models import Category

def menu_links(request):             #Funcion que nos permite ver que los links vendran de la base de datos y realizamos consulta
    links = Category.objects.all()
    return dict(links=links) #Retorna un diccionario con valor de links

#Se registra la fincion en la carpeta principal settings