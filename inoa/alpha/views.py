from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from multiprocessing import context
from django.views import generic

from .models import Acao, AcaoOwner

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm



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
    

class AcaoUserView(LoginRequiredMixin, generic.ListView):
  model = AcaoOwner
  paginate_by = 20

  def get_queryset(self):
    return AcaoOwner.objects.filter(owner=self.request.user)


def about(request):
  return render(request, 'about.html')


#class AcaoDonoCreate(LoginRequiredMixin, CreateView):
#    model = AcaoDono
#    fields = ['acao', 'owner', 'buy_price']

class CriarAcaoDono(View):

  def post(self, request):
    acao = request.POST.get("id_acao")
    price = request.POST.get("id_price")
    print(acao,price)
    return HttpResponseRedirect("/")

#def AcaoDonoCreate(request):
#  acao = request.POST.get("acao")
#  print(acao)
#  return HttpResponseRedirect("/")

#class AuthorDelete(LoginRequiredMixin, DeleteView):
#    model = Author
#    success_url = reverse_lazy('authors')
#    permission_required = 'catalog.can_mark_returned'