from pyexpat import model
from django.shortcuts import get_object_or_404, render
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

class AcaoDetailView(generic.DetailView):
  model = Acao

  def acao_datail_view(request, primary_key):
    acao = get_object_or_404(Acao, pk=primary_key)
    return render(request, 'alpha/acao_detail.html', context={'acao': acao})