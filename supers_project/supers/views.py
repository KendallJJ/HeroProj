# from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Supers
from django.urls import reverse


all_supers = Supers.objects.all()


def index(request):
    context = {
        'all_supers' : all_supers
    }
    return render(request, 'supers/index.html', context)

def detail(request, super_id):
        single_super = Supers.objects.filter(pk=super_id)
        context = {
            'single_super' : single_super
        }
        return render(request, 'supers/detail.html', context)



def create(request):
        if request.method == "POST":
            # Save the form contents as a new db object
            # return to index
            name = request.POST.get('name')
            alter_ego = request.POST.get('alter_ego')
            primary = request.POST.get('primary')
            secondary = request.POST.get('secondary')
            catchphrase = request.POST.get('catchphrase')
            new_super = Supers(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
            new_super.save()
            return HttpResponseRedirect(reverse('supers:index'))
        else:
            return render(request, 'supers/create.html')
        