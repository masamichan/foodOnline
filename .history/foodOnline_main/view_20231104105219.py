from django.shortscut import render
from django import HttpRespose
from . import view

def home(request):
  return HttptRespose('Hello Wrold')
