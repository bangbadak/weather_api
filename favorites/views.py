from django.shortcuts import render
from .models import Favorite
# Create your views here.
def index(request):
    fav = Favorite.objects.all()

    return render(
        request,
        'favorites/favorite.html',
        {
            'fav': fav
        }
    )