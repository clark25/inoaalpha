from django.apps import AppConfig


class AlphaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alpha'

    def ready(self):
        from acaoUpdater import updater
        updater.start()