import json
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

      
# def update_forecast():
#   json = _get_forecast_json()
#   if json is not None:
#     try:
#       new_forecast = Forecast()
            
#       #open weather map gives temps in Kelvin. We want celsius.              
#       temp_in_celsius = json['main']['temp'] - 273.15
#       new_forecast.temperatue = temp_in_celsius
#       new_forecast.description = json['weather'][0]['description']
#       new_forecast.city = json['name']
#       # temp_in_celsius = 294.99 - 273.15
#       # new_forecast.temperatue = temp_in_celsius
#       # new_forecast.description = "overcast clouds"
#       # new_forecast.city = "London"
#       new_forecast.save()
#     except:
#       pass

def update_acaoHistorico():
  
  for AcaoObj in Acao.objects.all():
    json = _get_acao_json(AcaoObj.symbol)
    if json is not None:
      try:
        new_AcaoHistorico = AcaoHistorico()


        new_AcaoHistorico.acao = AcaoObj.id
        new_AcaoHistorico.price = json['results'][AcaoObj.symbol.upper()]['price']
        new_AcaoHistorico.save()

        AcaoObj.last_price = json['results'][AcaoObj.symbol.upper()]['price']
        AcaoObj.save()

      except:
        pass