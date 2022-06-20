from django.contrib import admin

from transactions.models import Transaction, TransactionFileUpload, TransactionType


class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    fieldsets = [
        ("Transaction Type Information", {
            "fields": [
                "name"
            ],
            "classes": ["wide"]
        })
    ]


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "date", "transaction_type", "country", "currency", "net", "vat"
    ]
    list_display_links = [
        "date", "transaction_type", "country", "currency", "net", "vat"
    ]
    list_select_related = ["transaction_type"]
    list_filter = ["transaction_type"]
    search_fields = ["date", "country", "currency"]
    autocomplete_fields = ["transaction_type"]
    fieldsets = [
        ("Transaction Type Information", {
            "fields": ["transaction_type"],
            "classes": ["wide"]
        }),
        ("Transaction Information", {
            "fields": ["date", "country", "currency", "net", "vat"],
            "classes": ["wide"]
        })
    ]


class TransactionFileUploadAdmin(admin.ModelAdmin):
    list_display = ["name", "transaction_file"]
    list_display_links = ["name", "transaction_file"]
    search_fields = ["name"]
    fieldsets = [
        ("Transaction File Upload Information", {
            "fields": ["name", "transaction_file"],
            "classes": ["wide"]
        })
    ]


admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionFileUpload, TransactionFileUploadAdmin)
