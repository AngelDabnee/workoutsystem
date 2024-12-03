from django.db import models
from types_exercises.models import TypeExercise
from users.models import User

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='exercises', verbose_name='Imagen', null=True, blank=True)
    type_exercise_id = models.ForeignKey(TypeExercise, on_delete=models.CASCADE, verbose_name='Tipo de ejercicio')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")
    
        
    class Meta:
        verbose_name= "ejercicio"
        verbose_name_plural= "ejercicios"
        ordering=["-created"]
    
    
    def __str__(self):
        return self.name