
from rest_framework import serializers
from transaction.models import Transaction
from account.serializers import CategorySerializer, BankSerializer
from customer.serializers import CustomerSerializer
class TransactionSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    category = CategorySerializer()
    bank_account = BankSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'