from rest_framework import serializers
from account.models import Bank, Category

class BankSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Bank
        fields = '__all__'




class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new

    class Meta:
        model = Category
        fields = '__all__'


