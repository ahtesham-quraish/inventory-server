from rest_framework import serializers
from invoicce.models import InvoiceItems

class InvoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItems
        fields = ( 'id','overiddenPrice', 'quatityOffered')

