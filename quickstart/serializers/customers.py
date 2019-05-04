from rest_framework import serializers
from quickstart.models.customers import CustomerModel

class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = CustomerModel
        fields = '__all__'

