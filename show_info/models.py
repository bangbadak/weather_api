from django.db import models

# Create your models here.
class Province(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}_{self.pk}'

class City(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}_{Province.pk}_{self.pk}'

class County(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}_{City.pk}_{self.pk}'

