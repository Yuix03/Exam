from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Muallif(models.Model):

    name = models.CharField(max_length=50)
    y_old = models.PositiveIntegerField(default=True,blank=True)
    job = models.CharField(max_length=50,default=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name