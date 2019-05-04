from rest_framework import serializers
from quickstart.models.purchase import PurchaseModel

class PurchaseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = PurchaseModel
        fields = '__all__'

