
from django.http import HttpResponse
from . import views

def home(request):
  return (request, 'home.ht')
