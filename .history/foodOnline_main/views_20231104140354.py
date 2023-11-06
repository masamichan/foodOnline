from django.shotscut import render
from django.http import HttpResponse


def home(request):
  return render(request, 'home.html')
