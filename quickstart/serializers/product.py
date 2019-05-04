from rest_framework import serializers
from quickstart.models.product import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = ProductModel
        fields = ('id','title','description', 'size','brand', 'unit', 'owner', 'created', 'updated')

