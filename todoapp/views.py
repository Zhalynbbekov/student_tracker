from django.shortcuts import render
from .models import *


# Create your views here.
def say_hello(request):
    info = Information.objects.all()
    return render(request, 'index.html', {'info': info})

