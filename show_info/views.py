from django.shortcuts import render
from .models import Province, City, County

# Create your views here.
def index(request):
    provinces = Province.objects.all()
    cities = City.objects.all()
    counties = County.objects.all()
    print("provinces : ", provinces)
    return render(
        request,
        'show_info/index.html',
        {
            'provinces': provinces,
            'cities': cities,
            'counties': counties,
        },

    )