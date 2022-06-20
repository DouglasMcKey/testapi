from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from transactions.views import (
    TransactionFileUploadViewSet, TransactionsViewSet,
)

router = routers.DefaultRouter()
router.register(r"transactions", TransactionsViewSet)
router.register(r"transaction-upload", TransactionFileUploadViewSet)

urlpatterns = [
    path("administration/doc/", include("django.contrib.admindocs.urls")),
    path("administration/", admin.site.urls),
    path("", include(router.urls))
]
