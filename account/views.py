from django.shortcuts import render
from .models import ID


# Create your views here.
def id(request):

    id = ID.objects.all()
    return render(
        request,
        'account/account.html',
    )
