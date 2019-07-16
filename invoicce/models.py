from django.db import models
from product.models import Product
from customer.models import Customer
# Create your models here.
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


class InvoiceItems(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    overiddenPrice = models.IntegerField(default=0)
    quatityOffered = models.IntegerField(default=0)
    customerDescription = models.CharField(max_length=20)
