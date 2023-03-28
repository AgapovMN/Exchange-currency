from django.db import models

class ExchangeMarket(models.Model):
    marketname = models.CharField(max_length=150, verbose_name='Рынок обмена')
    api_url = models.CharField(max_length=150, verbose_name='API')

    class Meta:
        verbose_name = 'Рынок обмена'
        verbose_name_plural = 'Рынки обмена'
        ordering = ['pk']

    def __str__(self):
        return self.marketname

