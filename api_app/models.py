from django.db import models

# Create your models here.
class received_api(models.Model):
    avgTA = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    
