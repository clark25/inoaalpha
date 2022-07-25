from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from acaoUpdater import acaoApi

def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(acaoApi.update_acaoHistorico, 'interval', minutes=60)
  scheduler.start()
  