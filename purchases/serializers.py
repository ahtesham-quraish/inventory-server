from rest_framework import serializers
from purchases.models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Purchase
        fields = '__all__'

