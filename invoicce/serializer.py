from rest_framework import serializers
from invoicce.models import InvoiceItems
# from product.serializers import TopicRelatedField

class InvoiceItemsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = InvoiceItems
        fields = ( 'id','overiddenPrice', 'quatityOffered','product')

