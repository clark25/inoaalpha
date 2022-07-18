from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.
class Acao(models.Model):
  name = models.CharField(max_length=200)
  symbol = models.CharField(max_length=10)
  last_price = models.FloatField(default=0)

  def __str__(self):
    return self.name


class AcaoHistorico(models.Model):
  acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
  price = models.FloatField(default=0)
  date_price = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self) -> str:
    return super().__str__()