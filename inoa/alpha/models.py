from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User


# Create your models here.
class Acao(models.Model):
  name = models.CharField(max_length=200)
  symbol = models.CharField(max_length=10)
  last_price = models.FloatField(default=0)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('acao-detail', args=[str(self.id)])


class AcaoHistorico(models.Model):
  acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
  price = models.FloatField(default=0)
  date_price = models.DateTimeField('date published')

  def __str__(self) -> str:
    return super().__str__()

  class Meta:
    ordering = ['-date_price']

class AcaoDono(models.Model):
  acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  buy_price = models.FloatField(default=0)
  date_buy = models.TimeField(auto_now_add=True, default = 'time created'),

  def __str__(self) -> str:
    return super().__str__()
  
  def get_absolute_url(self):
    return reverse('acao-detail', args=[str(self.id)])