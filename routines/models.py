from django.db import models
from exercises.models import Exercise
from users.models import User
# Create your models here.

class Routine(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='routines', verbose_name='Imagen', null=True, blank=True)
    exercises = models.ManyToManyField(Exercise, verbose_name='Ejercicios')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")
    
        
    class Meta:
        verbose_name= "rutina"
        verbose_name_plural= "rutinas"
        ordering=["-created"]
    
    
    def __str__(self):
        return self.name
