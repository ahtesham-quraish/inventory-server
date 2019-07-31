from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from invoicce.models import Invoice,InvoiceItems
from product.models import Product
from customer.models import Customer
from product.serializers import ProductSerializer
from django.core.mail import EmailMessage
import os
from tutorial.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
from customer.models import Customer
from invoicce.serializer import InvoiceItemsSerializer
# Create your views here.
import traceback
from django.db import transaction

class InvoiceView(APIView):
    def get(self,request):
        invoice_id = request.data.get('invoice_id')
        cust_id = request.data.get('cust_id')
        if invoice_id is None:
            if cust_id:
                cust_set = Customer.objects.filter(id=cust_id)
                invoices_set = Invoice.objects.all(customer=cust_set[0]).select_related("customer")
                invoices = []
                print("invoices are ", invoices_set)
                for invoice in invoices_set:
                    invoice_items = InvoiceItems.objects.filter(invoice=invoice)
                    invoice_temp = {
                        "id": invoice.id,
                        "customer": invoice.customer.fName + " " + invoice.customer.lName,
                        "products": InvoiceItemsSerializer(invoice_items, many=True).data,
                        "dateCreated": invoice.created
                    }
                    print("temp is ", invoice_temp)
                    invoices.append(invoice_temp)

                return Response({"invoices": invoices})
            else:
                invoices_set = Invoice.objects.all().select_related("customer")
                invoices = []
                print("invoices are ", invoices_set)
                for invoice in invoices_set:
                    invoice_items = InvoiceItems.objects.filter(invoice=invoice)
                    invoice_temp = {
                        "id": invoice.id,
                        "customer": invoice.customer.fName + " " + invoice.customer.lName,
                        "products": InvoiceItemsSerializer(invoice_items, many=True).data,
                        "dateCreated": invoice.created
                    }
                    print("temp is ", invoice_temp)
                    invoices.append(invoice_temp)

                return Response({"invoices": invoices})
        else:
            pass



        # invoices = Invoice.objects.all().select_related('customer')
        # invoice_list = []
        # if invoices:
        #     for invoice in invoices:
        #         items = []
        #         invoice_items = InvoiceItems.objects.filter(invoice=invoice).select_related('product')
        #         if invoice_items:
        #             for item in invoice_items:
        #                 temp={
        #                     'brand': item.product.brand,
        #                     'created':item.product.created,
        #                     'custDescription':item.customerDescription,
        #                     'description':item.product.description,
        #                     'id':item.product.id,
        #                     'price':item.product.price,
        #                     'qoutedPrice':item.overiddenPrice,
        #                     'quatity':item.product.quatity,
        #                     'requiredQty':item.quatityOffered,
        #                     'size':item.product.size,
        #                     'title':item.product.title,
        #                     'unit':item.product.unit,
        #                     'updated':item.product.updated
        #                 }
        #                 items.append(temp)
        #
        #             temp = {
        #                 'id': invoice.id,
        #                 'dateCreated': invoice.created,
        #                 'cutsomer': {
        #                     'Address1': invoice.customer.Address1,
        #                     'Address2': invoice.customer.Address2,
        #                     'Phone': invoice.customer.Phone,
        #                     'city': invoice.customer.city,
        #                     'company_name': invoice.customer.company_name,
        #                     'country': invoice.customer.country,
        #                     'created': invoice.customer.created,
        #                     'description': invoice.customer.description,
        #                     'email': invoice.customer.email,
        #                     'fName': invoice.customer.fName,
        #                     'id': invoice.customer.id,
        #                     'lName': invoice.customer.lName,
        #                     'postal_code': invoice.customer.postal_code
        #                 },
        #                 'products': items
        #             }
        #
        # return Response({"status":200,"invoices":invoice_list})


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
                "id":item.id,
                "original_product":product_data.data,
                "added_info":{
                    'custDescription': item.customerDescription,
                    'qoutedPrice': item.overiddenPrice,
                    'requiredQty': item.quatityOffered,
                }
            }
            invoice_products.append(temp)
        return Response({"status":status.HTTP_201_CREATED,"products":invoice_products})


class EmailInvoice(APIView):

    def post(self,request):
        user_id = request.data.get('user_id')
        file = request.FILES.get('file')
        if user_id is None:
            return Response({
                "status":status.HTTP_406_NOT_ACCEPTABLE,
                "message":"All fields are required"
            })
        if file is None:
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": "All fields are required"
            })
        try:
            customer = Customer.objects.filter(id=user_id)
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            print("sending to ",customer[0].email)
            email = EmailMessage(
                'Hello',
                'Body goes here',
                'samaid2025@gmail.com',
                [customer[0].email],
                ['samaid2025@gmail.com'],
                reply_to=['samaid2025@gmail.com'],
                headers={'Message-ID': 'foo'},
            )
            print(MEDIA_ROOT)
            email.attach_file(MEDIA_ROOT + '/' + filename)
            email.send(fail_silently=False)
            return Response({"status": status.HTTP_200_OK,
                "message": "Qoutation emailed to customer"})
        except:
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Qoutation could not be emailed"
            })

