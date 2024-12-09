from django.db import models
from exercises.models import Exercise
from users.models import User
# Create your models here.

class ExerciseUser(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name='Ejercicio')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de modificación")
    
        
    class Meta:
        verbose_name= "ejercicio_usuario"
        verbose_name_plural= "ejercicios_usuarios"
        ordering=["-created"]
    
    
    def __str__(self):
        return self.exercise_id.name