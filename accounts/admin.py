from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name','last_name', 'username', 'last_login', 'date_joined', 'is_active' )
    list_display_links = ('email', 'first_name', 'last_name') #Cuando el usuario da clic este link envie al detalle del usuario
    readonly_fields = ('last_login', 'date_joined') #La ultima vez que se unieron
    ordering = ('-date_joined',) #Cuando se unio a la aplicacion
    
    filter_horizontal = () #Ordenar lista
    list_filter = ()
    fieldsets = ()
    
    

# Register your models here.
admin.site.register(Account, AccountAdmin)