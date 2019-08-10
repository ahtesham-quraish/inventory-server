from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Customer
        fields = '__all__'

