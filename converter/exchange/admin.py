from django.contrib import admin

from .models import ExchangeMarket

class ExchangeMarketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'marketname', 'api_url')
    list_display_links = ('marketname', 'pk')


admin.site.register(ExchangeMarket, ExchangeMarketAdmin)