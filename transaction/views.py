
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework import generics, permissions # new
class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Create your views here.
