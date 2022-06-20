import csv
import io

from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from transactions.models import (
    Transaction, TransactionFileUpload, TransactionType
)
from transactions.utilities import save_transaction_data


class TransactionTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TransactionType
        fields = ["id", "url", "name", "notes"]


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            "id", "url", "transaction_type", "country", "currency",
            "date", "net", "vat"
        ]


class TransactionFileUploadSerializer(serializers.ModelSerializer):
    transaction_file = serializers.FileField(
        validators=[FileExtensionValidator(["csv"])]
    )

    class Meta:
        model = TransactionFileUpload
        fields = ["id", "name", "transaction_file"]

    def create(self, validated_data):
        file_object = validated_data["transaction_file"]
        file = file_object.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]

        # Send the data to the function that will populate the database.
        save_transaction_data(data, 2020, currency_denominator="EUR")

        return TransactionFileUpload.objects.create(**validated_data)
