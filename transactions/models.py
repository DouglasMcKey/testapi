from django.core.validators import FileExtensionValidator
from django.db import models
from django_countries.fields import CountryField


class TransactionType(models.Model):
    name = models.CharField(
        max_length=64
    )
    notes = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = "Transaction Type"
        verbose_name_plural = "Transaction Types"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    transaction_type = models.ForeignKey(
        TransactionType,
        verbose_name="Transaction Type",
        on_delete=models.CASCADE
    )
    country = CountryField()
    currency = models.CharField(
        max_length=3
    )
    date = models.DateField(
        "Transaction Date",
        null=True,
        blank=True,
        help_text="Transaction date is in the following format e.g.: yyyy-mm-dd."
    )
    net = models.DecimalField(
        "Net",
        max_digits=12,
        decimal_places=2,
        default=0.00
    )
    vat = models.DecimalField(
        "VAT",
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ["date", "transaction_type", "net"]

    def __str__(self):
        return f"{self.transaction_type} {self.net} {self.currency} ({self.date})"


class TransactionFileUpload(models.Model):
    name = models.CharField(
        max_length=256
    )
    transaction_file = models.FileField(
        upload_to="transactions/uploads/",
        validators=[FileExtensionValidator(["csv"])]
    )

    class Meta:
        verbose_name = "Transaction File Upload"
        verbose_name_plural = "Transaction File Uploads"

    def __str__(self):
        return f"{self.transaction_file}"
