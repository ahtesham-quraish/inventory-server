from rest_framework import serializers
from invoicce.models import InvoiceItems, Invoice
from product.serializers import ProductSerializer
from customer.serializers import CustomerSerializer

class InvoiceSerlializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Invoice
        fields = ('id','buyerOrderNumber','buyerOrderNumberDate','taxInvoiceNumber','taxInvoiceNumberDate'
                  ,'deliverNumber','deliverNumberDate','qoutNumber','qoutNumberDate','subTotal','grandTotal',
                  'discount','status','residualPayment','customer')

class InvoiceItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    invoice = InvoiceSerlializer()

    class Meta:
        model = InvoiceItems
        fields = ( 'id','overiddenPrice', 'quatityOffered','customerDescription','product', 'invoice')

