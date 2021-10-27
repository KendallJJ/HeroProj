from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Supers
all_supers = Supers.objects.all()


def index(request):
    context = {
        'all_supers' : all_supers
    }
    return render(request, 'supers/index.html', context)