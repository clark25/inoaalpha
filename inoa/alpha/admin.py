from django.contrib import admin

from .models import Acao, AcaoHistorico, AcaoDono
# Register your models here.
class AcaoHistoricoInline(admin.TabularInline):
  """Defines format of inline AcaoHistorico insertion"""
  model = AcaoHistorico
  extra = 1

class AcaoDonoInline(admin.TabularInline):
  """Defines format of inline AcaoDono insertion"""
  model = AcaoDono
  extra = 1


@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
  """Administration object for Acao models."""
  inlines = [AcaoHistoricoInline, AcaoDonoInline]
  search_fields = ['name']