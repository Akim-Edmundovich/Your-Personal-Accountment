from rest_framework import viewsets
from apps.transactions.api.serializers import TransactionSerializer, CategorySerializer, \
    SubcategorySerializer
from apps.transactions.models import Category, Subcategory, Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
