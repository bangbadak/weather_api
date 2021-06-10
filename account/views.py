from django.shortcuts import render, redirect
from .models import ID


# Create your views here.
def id(request):
        id = ID.objects.get()
        return render(
            request,
            'account/account.html',
        )