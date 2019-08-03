from rest_framework import serializers
from account.models import Bank, Transaction

class BankSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Bank
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new

    class Meta:
        model = Transaction
        fields = '__all__'

