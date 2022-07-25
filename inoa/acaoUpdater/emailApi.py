from email import message
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User
from alpha.models import AcaoHistorico, Acao

def funcao_test():
  for usuario in User.objects.all():
    print(usuario.email)


def enviaEmail():
  emails = []
  comprarList = []
  venderList = []

  for usuario in User.objects.all():
    emails.append(usuario.email)


  for AcaoObj in Acao.objects.all():
    AcaoHistoricoList = AcaoHistorico.objects.filter(acao=AcaoObj)
    price_previous = AcaoHistoricoList[1].price
    price_atual= AcaoObj.last_price

    if((price_atual - price_previous) > 0):
      venderList.append(AcaoObj.name)
    
    elif((price_atual - price_previous) < 0):
      comprarList.append(AcaoObj.name)

  if(comprarList):
    stringComprarList = ' '.join(map(str,comprarList))

    send_mail(
      subject= "INOA ALPHA - Compre essas ações agora!",
      message= "O preço dessas ações caiu, talvez seja hora de adiciona-las a sua carteira"+stringComprarList,
      from_email=settings.EMAIL_HOST_USER,
      recipient_list=emails
    )

  if(venderList):
    stringVenderList = ' '.join(map(str,venderList))

    send_mail(
      subject= "INOA ALPHA - Venda essas ações agora!",
      message= "O preço dessas ações subiu, talvez seja hora de vende-las e ter um excelente lucro"+stringVenderList,
      from_email=settings.EMAIL_HOST_USER,
      recipient_list=emails
    )
    