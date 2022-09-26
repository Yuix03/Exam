from django.db import models

# Create your models here.
from userapp.models import Muallif


class Blog(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=40)
    text = models.TextField()
    user = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
