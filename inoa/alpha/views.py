from django.shortcuts import render
from multiprocessing import context
from django.views import generic

from .models import Acao

# Create your views here.
def index(request):
  """View function for home page of site."""
  return render(request, 'index.html')


class AcaoListView(generic.ListView):
  model = Acao
  paginate_by = 20