from account.models import Bank, Transaction
from account.serializers import BankSerializer, TransactionSerializer
from rest_framework import generics, permissions # new

class BankView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
