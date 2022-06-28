from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_recipe(filter_recipe = None):
    if filter_recipe:
        recipe = Recepi.objects.filter(name__contains = filter_recipe)
    else:
        # recipe = Recepi.objects.filter(name='lassi').first()   
        recipe = Recepi.objects.all() 
    print("data coming from database")
    return recipe


def home(request):
    filter_recipe = request.GET.get("recipe")
    if cache.get(filter_recipe):
        print("data coming from cache")
        recipe = cache.get(filter_recipe)
    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter, filter_recipe)
        else:
            recipe = get_recipe()
    context = {'recipe':recipe}
    return render(request, 'home.html', context)


def show(request, id):
    if cache.get(id):
        print("data coming from cache")
        recipe = cache.get(id)
    else:
        print("data coming from database")
        recipe = Recepi.objects.get(id=id)
    context = {"recipe":recipe}
    return render(request, 'show.html', context )

