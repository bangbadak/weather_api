from django.db import models
from django.db.models.fields import CharField, DecimalField

# Create your models here.
class Weather(models.Model):
    stnId = CharField(max_length=20, default='')
    avgTA = DecimalField(decimal_places=1, max_digits=2)
    