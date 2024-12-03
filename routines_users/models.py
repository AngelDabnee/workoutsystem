from django.db import models
from users.models import User
from routines.models import Routine
# Create your models here.

class RoutineUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    routine_id = models.ForeignKey('routines.Routine', on_delete=models.CASCADE, verbose_name='Rutina')