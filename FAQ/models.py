from django.db import models

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(max_length=50)
    answer = models.TextField()

    def __str__(self):
        return f'{self.title}'
