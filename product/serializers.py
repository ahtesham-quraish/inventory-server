from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Product
        fields = ('id','title','description', 'size','brand', 'unit', 'owner', 'created', 'updated')

