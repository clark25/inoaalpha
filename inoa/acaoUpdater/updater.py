from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from acaoUpdater import acaoApi, emailApi

def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(acaoApi.update_acaoHistorico, 'interval', minutes=120)
  scheduler.add_job(emailApi.enviaEmail, 'interval', minutes=120)
  scheduler.start()
  