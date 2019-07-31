from rest_framework import serializers
from invoicce.models import InvoiceItems
from product.serializers import ProductSerializer

class InvoiceItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = InvoiceItems
        fields = ( 'id','overiddenPrice', 'quatityOffered','product')

