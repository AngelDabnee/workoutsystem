from django.db import models
from exercises.models import Exercise
from routines.models import Routine

# Create your models here.
class ExerciseRoutine(models.Model):
    exercise_id = models.ForeignKey('exercises.Exercise', on_delete=models.CASCADE, verbose_name='Ejercicio')
    routine_id = models.ForeignKey('routines.Routine', on_delete=models.CASCADE, verbose_name='Rutina')