from django.urls.resolvers import URLPattern
from . import views
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path

app_name = 'supers'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:super_id>/', views.detail, name = 'detail'),
    path('new/', views.create, name = 'create')

]