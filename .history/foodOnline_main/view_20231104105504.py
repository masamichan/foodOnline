from django.shortscut import render
from django import HttpRespose
from . import view

def home(request):
  return HttpRespose('Hello World')
