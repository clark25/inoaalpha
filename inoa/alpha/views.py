from django.shortcuts import render
from multiprocessing import context
from django.views import generic

# Create your views here.
def index(request):
  """View function for home page of site."""
  return render(request, 'index.html')