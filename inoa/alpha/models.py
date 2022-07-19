from django.db import models

from django.contrib.auth.models import User


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
  date_price = models.DateTimeField('date published')

  def __str__(self) -> str:
    return super().__str__()


class AcaoDono(models.Model):
  acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  buy_price = models.FloatField(default=0)
  date_buy = models.DateTimeField('date published')

  def __str__(self) -> str:
    return super().__str__()