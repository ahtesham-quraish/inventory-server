
from rest_framework import serializers
from transaction.models import Transaction
from account.serializers import CategorySerializer, BankSerializer
from customer.serializers import CustomerSerializer
class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    bank_account = BankSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'