from django.db import models


class ExchangeRateHistory(models.Model):
    currency = models.CharField(
        max_length=3
    )
    currency_denominator = models.CharField(
        max_length=3
    )
    exchange_rate = models.DecimalField(
        "Exchange Rate",
        max_digits=12,
        decimal_places=5,
        default=0.00
    )
    observation_date = models.DateField()

    class Meta:
        verbose_name = "Exchange Rate History"
        verbose_name_plural = "Exchange Rate History"
        ordering = ["currency", "observation_date"]

    def __str__(self):
        return f"{self.currency} > {self.currency_denominator}:" \
               f" {self.exchange_rate} ({self.observation_date})"
