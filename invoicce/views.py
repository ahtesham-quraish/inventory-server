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
from invoicce.serializer import InvoiceItemsSerializer, InvoiceSerlializer
# Create your views here.
import traceback
from django.db import transaction
from django.db.models import Q

class InvoiceView(APIView):
    def get(self,request):
        invoice_id = request.GET.get('invoice_id')
        cust_id = request.GET.get('cust_id')
        print("cust id is ", invoice_id)
        if invoice_id is None:

            if cust_id:
                print("getting for cust")
                cust_set = Customer.objects.filter(id=cust_id)
                invoices_set = Invoice.objects.filter(customer=cust_set[0]).select_related("customer")
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
            products = []
            invoices_set = Invoice.objects.filter(id=invoice_id).select_related("customer")
            if invoices_set:
                invoice_items = InvoiceItems.objects.filter(invoice=invoices_set[0])
                if invoice_items:
                    invoice_data = InvoiceSerlializer(invoices_set,many=True)
                    products = InvoiceItemsSerializer(invoice_items,many=True)
                    temp = {
                        "invoice":invoice_data.data[0],
                        "products":products.data
                    }
                    return Response(temp)

    def delete(self,request):
        invoice_id = request.GET.get("invoice_id")

        if invoice_id:
            target_invoice = Invoice.objects.filter(id=invoice_id)
            if(target_invoice):
                target_invoice.delete()
                return Response({"status": 200,"message":"invoice deleted"})
            else:
                return Response({"status": 414,"message":"invoice does not exist"})
            
        else:
            return Response({"status": 200,"message":"invoice id missing"})

    def put(self,request):
        invoice_id = request.data.get('id')
        status = request.data.get('status')
        amount = request.data.get('amount')

        invoice = Invoice.objects.filter(id=invoice_id)
        if invoice:
            invoice[0].status = status
            invoice[0].residualPayment = amount
            invoice[0].save()
            return Response({"status": 200})
        else:
            return Response({"status": 404})




    def post(self,request):
        products = request.data.get('products')
        customer = request.data.get('customer')
        invoiceInputs = request.data.get('invoiceInputs')
        customer_instance = Customer.objects.filter(id=customer["id"])
        print("invoice input is ",invoiceInputs['status'])
        try:
            
            with transaction.atomic():
                Invoice_Inctance = Invoice.objects.create(customer=customer_instance[0],buyerOrderNumber=invoiceInputs['buyerOrderNumber'],
                                                    buyerOrderNumberDate=invoiceInputs['buyerOrderNumberDate'],
                                                    taxInvoiceNumber=invoiceInputs['taxInvoiceNumber'],
                                                    taxInvoiceNumberDate=invoiceInputs['taxInvoiceNumberDate'],
                                                    deliverNumber=invoiceInputs['deliverNumber'],
                                                    deliverNumberDate=invoiceInputs['deliverNumberDate'],
                                                    qoutNumber=invoiceInputs['qoutNumber'],
                                                    qoutNumberDate=invoiceInputs['qoutNumberDate'],
                                                          subTotal=invoiceInputs['subTotal'],
                                                          grandTotal=invoiceInputs['grandTotal'],
                                                          discount=invoiceInputs['discount'],
                                                          status=invoiceInputs['status'],
                                                          )
                for product in products:
                    product_instance = Product.objects.filter(id=product['id'])
                    if product_instance:
                        InvoiceItems.objects.create(invoice=Invoice_Inctance,
                                                    product=product_instance[0],
                                                    overiddenPrice=product['qoutedPrice'],
                                                    quatityOffered=product['requiredQty'],
                                                    customerDescription=product['custDescription'],


                                                    )
                return Response({"status": status.HTTP_201_CREATED})

        except:

            traceback.print_exc()
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

