from django.contrib import admin
from .models import Province, City, County

# Register your models here.
admin.site.register(Province)
admin.site.register(City)
admin.site.register(County)