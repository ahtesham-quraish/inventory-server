from django.db import models
from account.models import Category


class Customer(models.Model):
    fName = models.CharField(max_length=20, default='Pakistan', null=True, blank=True)
    lName = models.CharField(max_length=20, default='Pakistan', null=True, blank=True)
    Address1 = models.CharField(max_length=300, default=None, null=True, blank=True)
    Address2 = models.CharField(max_length=300, default=None, null=True, blank=True)
    Phone  = models.IntegerField(default=None, null=True, blank=True)
    postal_code = models.CharField(max_length=20, default=None, null=True, blank=True)
    city = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  default='1')
    country  = models.CharField(max_length=20, default='Pakistan', null=True, blank=True)
    email = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=200, default=None, null=True, blank=True)
    description = models.CharField(max_length=200, default=None, null=True, blank=True)
    gst = models.CharField(max_length=50, default='')
    ntn = models.CharField(max_length=50, default='')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.fName +" "+self.lName