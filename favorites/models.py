from django.db import models

# Create your models here.
class Favorite(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'
