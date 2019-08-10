from django.db import models
from product.models import Product
from customer.models import Customer
# Create your models here.
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    buyerOrderNumber = models.CharField(max_length=20, default="", null=True, blank=True)
    buyerOrderNumberDate = models.CharField(max_length=20, default="", null=True, blank=True)
    taxInvoiceNumber = models.CharField(max_length=20, default="", null=True, blank=True)
    taxInvoiceNumberDate = models.CharField(max_length=20, default="", null=True, blank=True)
    deliverNumber = models.CharField(max_length=20, default="", null=True, blank=True)
    deliverNumberDate = models.CharField(max_length=20, default="", null=True, blank=True)
    qoutNumber = models.CharField(max_length=20, default="", null=True, blank=True)
    qoutNumberDate = models.CharField(max_length=20, default="", null=True, blank=True)
    residualPayment = models.IntegerField(default = 0, null=True, blank=True)
    subTotal = models.IntegerField(default = 0, null=True, blank=True)
    grandTotal = models.IntegerField(default = 0, null=True, blank=True)
    discount = models.IntegerField(default = 0, null=True, blank=True)
    status = models.CharField(max_length=20, default="Unpaid", null=True, blank=True)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)



class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    overiddenPrice = models.IntegerField(default=0)
    quatityOffered = models.IntegerField(default=0)
    customerDescription = models.CharField(max_length=20)
