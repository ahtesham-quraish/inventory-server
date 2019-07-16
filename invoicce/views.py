from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from invoicce.models import Invoice,InvoiceItems
from product.models import Product
from customer.models import Customer
from product.serializers import ProductSerializer
# Create your views here.
import traceback
from django.db import transaction

class InvoiceView(APIView):
    def get(self,request):
        invoices = Invoice.objects.all().select_related('customer')
        invoice_list = []
        if invoices:
            for invoice in invoices:
                items = []
                invoice_items = InvoiceItems.objects.filter(invoice=invoice).select_related('product')
                if invoice_items:
                    for item in invoice_items:
                        temp={
                            'brand': item.product.brand,
                            'created':item.product.created,
                            'custDescription':item.customerDescription,
                            'description':item.product.description,
                            'id':item.product.id,
                            'price':item.product.price,
                            'qoutedPrice':item.overiddenPrice,
                            'quatity':item.product.quatity,
                            'requiredQty':item.quatityOffered,
                            'size':item.product.size,
                            'title':item.product.title,
                            'unit':item.product.unit,
                            'updated':item.product.updated
                        }
                        items.append(temp)
                        temp={
                            'id':invoice.id,
                            'cutsomer':{
                              'Address1':invoice.customer.Address1,
                                'Address2':invoice.customer.Address2,
                                'Phone':invoice.customer.Phone,
                                'city':invoice.customer.city,
                                'company_name':invoice.customer.company_name,
                                'country':invoice.customer.country,
                                'created':invoice.customer.created,
                                'description':invoice.customer.description,
                                'email':invoice.customer.email,
                                'fName':invoice.customer.fName,
                                'id':invoice.customer.id,
                                'lName':invoice.customer.lName,
                                'postal_code':invoice.customer.postal_code
                            },
                            'products':items
                        }
                        invoice_list.append(temp)
                        items=[]
        return Response({"status":200,"invoices":invoice_list})


    def post(self,request):
        products = request.data.get('products')
        customer = request.data.get('customer')
        customer_instance = Customer.objects.filter(id=customer["id"])
        print (customer_instance)
        try:
            
            with transaction.atomic():
                Invoice_Inctance = Invoice.objects.create(customer=customer_instance[0])
                for product in products:
                    product_instance = Product.objects.filter(id=product['id'])
                    if product_instance:
                        InvoiceItems.objects.create(invoice=Invoice_Inctance,
                                                    product=product_instance[0],
                                                    overiddenPrice=product['qoutedPrice'],
                                                    quatityOffered=product['requiredQty'],
                                                    customerDescription=product['custDescription']
                                                    )
                return Response({"status": status.HTTP_201_CREATED})

        except:
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR})


class InvoiceByCustomer(APIView):

    def get(self,request):
        cust_id = request.GET.get('cust_id')
        print(cust_id)
        cust_instance = Customer.objects.filter(id=cust_id)
        print(cust_instance)
        invoiceItems = InvoiceItems.objects.filter(invoice__customer=cust_instance[0]).select_related('invoice','product')
        invoice_products = []
        for item in invoiceItems:
            product_data = ProductSerializer(item.product, many=False)
            temp = {
                "original_product":product_data.data,
                "added_info":{
                    'custDescription': item.customerDescription,
                    'qoutedPrice': item.overiddenPrice,
                    'requiredQty': item.quatityOffered,
                }
            }
            invoice_products.append(temp)
        return Response({"status":status.HTTP_201_CREATED,"products":invoice_products})
