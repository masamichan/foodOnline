from django.shotscat import render
from django.http import HttpResponse
from . import views

def home(request):
  return (request, 'home.html')
