from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('acao/', views.AcaoListView.as_view(), name='acao'),
]