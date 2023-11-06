from django.shortscut import render
from django.http import HttpResponse
from . import views

def home(request):
  return HttpResponse('Hello World')
