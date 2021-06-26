from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ID(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    def __str__(self):
        return f'ID_{self.pk}'
