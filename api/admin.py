from django.contrib import admin

from api.models import ExchangeRateHistory


class ExchangeRateHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "currency", "currency_denominator", "exchange_rate", "observation_date"
    ]
    list_display_links = [
        "currency", "currency_denominator", "exchange_rate", "observation_date"
    ]
    search_fields = ["currency", "currency_denominator"]
    fieldsets = [
        ("Exchange Rate History Date Information", {
            "fields": [
                "observation_date"
            ],
            "classes": ["wide"]
        }),
        ("Exchange Rate History Information", {
            "fields": [
                "currency", "currency_denominator", "exchange_rate"
            ],
            "classes": ["wide"]
        })
    ]


admin.site.register(ExchangeRateHistory, ExchangeRateHistoryAdmin)
