from django.db import models
from customer.models import Customer
from account.models import Category
from account.models import Bank
# Create your models here.

class Transaction(models.Model):
    bank_account = models.ForeignKey(Bank, on_delete=models.CASCADE)
    date = models.CharField(max_length=20, default="", null=True, blank=True)
    type = models.CharField(max_length=20, default="", null=True, blank=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE,  default='1' )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,  default=2)
    description = models.CharField(max_length=20, default="", null=True, blank=True)
    amount = models.CharField(max_length=20, default="", null=True, blank=True)

    def __unicode__(self):
        return self.bank_account
