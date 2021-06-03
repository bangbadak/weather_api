from django.shortcuts import render
from .models import FAQ

# Create your views here.
def index(request):
    faq = FAQ.objects.all()

    return render(
        request,
        'FAQ/FAQ.html',
        {
            'faq': faq,
        },

    )
