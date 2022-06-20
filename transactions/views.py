from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from transactions.models import (
    Transaction, TransactionFileUpload, TransactionType
)
from transactions.serializers import (
    TransactionFileUploadSerializer, TransactionSerializer,
    TransactionTypeSerializer
)


class TransactionTypeViewSet(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all().order_by("name")
    serializer_class = TransactionTypeSerializer


class TransactionFileUploadViewSet(viewsets.ModelViewSet):
    queryset = TransactionFileUpload.objects.all().order_by("-pk")
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = TransactionFileUploadSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("pk")
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country", "date"]
