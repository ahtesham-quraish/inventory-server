from django.db import models
from customer.models import Customer
from account.models import Category
from account.models import Bank
from invoicce.models import Invoice
# Create your models here.

class Transaction(models.Model):
    bank_account = models.ForeignKey(Bank, related_name='bank', on_delete=models.CASCADE, blank=True,
        null=True)
    date = models.CharField(max_length=20,  default="", null=True, blank=True)
    type = models.CharField(max_length=20, default="", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True )
    invoiceId = models.CharField(max_length=20, default='', null=True, blank=True)
    customer = models.ForeignKey(Customer, related_name='cust', on_delete=models.CASCADE,  blank=True,
        null=True)
    description = models.CharField(max_length=20, default="", null=True, blank=True)
    amount = models.CharField(max_length=20, default="", null=True, blank=True)
    isSuperAdmin = models.BooleanField(default=True)

