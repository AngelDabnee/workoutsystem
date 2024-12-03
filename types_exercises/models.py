from django.db import models
# Create your models here.

class TypeExercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")
    
        
    class Meta:
        verbose_name= "tipo de ejercicio"
        verbose_name_plural= "tipos de ejercicios"
        ordering=["-created"]
    
    
    def __str__(self):
        return self.name