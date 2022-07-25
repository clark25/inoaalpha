import requests
from alpha.models import AcaoHistorico, Acao


def _get_acao_json(acaoSymbol):
  url = "https://api.hgbrasil.com/finance/stock_price?"
  key = "3afdaffb"
  pesquisa = acaoSymbol

    #https://api.hgbrasil.com/finance/stock_price?key=3afdaffb&symbol=PETR4

  response = requests.get('{0}key={1}&symbol={2}'.format(
    url,
    key,
    pesquisa
  ))

  try:
    response.raise_for_status()
    return response.json()
  except:
    return None


def update_acaoHistorico():
  
  for AcaoObj in Acao.objects.all():
    busca = AcaoObj.symbol
    json = _get_acao_json(busca)
    if json is not None:
      try:
        new_AcaoHistorico = AcaoHistorico()

        new_AcaoHistorico.acao = AcaoObj
        new_AcaoHistorico.price = json['results'][AcaoObj.symbol.upper()]['price']
        new_AcaoHistorico.save()
        

        AcaoObj.last_price = json['results'][AcaoObj.symbol.upper()]['price']
        AcaoObj.save()

      except:
        pass