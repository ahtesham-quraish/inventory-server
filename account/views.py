from account.models import Bank, Category
from account.serializers import BankSerializer, CategorySerializer
from rest_framework import generics, permissions # new


class BankView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


