from django.urls.resolvers import URLPattern
from . import views
from django.http import HttpResponse
from django.urls import path

app_name = 'supers'

urlpatterns = [
    path('', views.index, name = 'index')
]