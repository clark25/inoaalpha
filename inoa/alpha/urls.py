from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('acoes/', views.AcaoListView.as_view(), name='acoes'),
  path('acao/<int:pk>', views.AcaoDetailView.as_view(), name='acao-detail'),
]