from django.db import models
from roles.models import Role
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(unique=True, verbose_name='Correo')
    phone = models.CharField(max_length=15, verbose_name='Teléfono')
    password = models.CharField(max_length=100, verbose_name='Contraseña')
    image = models.ImageField(upload_to='users', verbose_name='Imagen', null=True, blank=True)  # Opcional
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')  # Rol del usuario
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")

        
    class Meta:
        verbose_name= "usuario"
        verbose_name_plural= "usuarios"
        ordering=["-created"]
    
    
    def __str__(self):
        return self.name
    
    
    
    

