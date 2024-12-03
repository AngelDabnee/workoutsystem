from django.db import models

# Create your models here.
class Role(models.Model):
    level = models.CharField(max_length=50, verbose_name='Nivel') 
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")    

    def __str__(self):
        return self.level