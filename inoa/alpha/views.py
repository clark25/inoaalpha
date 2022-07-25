from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from multiprocessing import context
from django.views import View, generic

from .models import Acao, AcaoDono

from django.contrib.auth.mixins import LoginRequiredMixin


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
  model = AcaoDono
  paginate_by = 20

  def get_queryset(self):
    return AcaoDono.objects.filter(owner=self.request.user)


def about(request):
  return render(request, 'about.html')


#class AcaoDonoCreate(LoginRequiredMixin, CreateView):
 #   model = AcaoDono
#    fields = ['acao', 'owner']

class CriarAcaoDono(LoginRequiredMixin,View):

  def post(self, request):
    new_acaodono = AcaoDono()
    new_acaodono.acao = Acao.objects.get(pk=request.POST.get("id_acao"))
    new_acaodono.owner = self.request.user
    price = request.POST.get("id_price")
    new_acaodono.price = float(price.replace(',','.'))
    new_acaodono.save()

    return HttpResponseRedirect("/alpha/acoesusuario/")

class ApagarAcaoDono(LoginRequiredMixin, View):
  def post(self, request):
    acaoId = request.POST.get("id_acaodono")
    acaoDel = AcaoDono.objects.get(id=acaoId)
    acaoDel.delete()

    return HttpResponseRedirect("/alpha/acoesusuario/")

#class AuthorDelete(LoginRequiredMixin, DeleteView):
#    model = Author
#    success_url = reverse_lazy('authors')
#    permission_required = 'catalog.can_mark_returned'