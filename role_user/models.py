from django.db import models
from roles.models import Role
from users.models import User
# Create your models here.


class RoleUser(models.Model): 
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")
    
        
    class Meta:
        verbose_name= "rol_usuario"
        verbose_name_plural= "roles_usuarios"
        ordering=["-created"]
    
    
    def __str__(self):
        return self.role_id.name
