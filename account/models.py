from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=20, default="", null=True, blank=True)
    code = models.CharField(max_length=20, default="", null=True, blank=True)
    entry_method = models.CharField(max_length=20, default="", null=True, blank=True)


class Transaction(models.Model):
    bank_account = models.ForeignKey(Bank, on_delete=models.CASCADE)
    date = models.CharField(max_length=20, default="", null=True, blank=True)
    type = models.CharField(max_length=20, default="", null=True, blank=True)
    category = models.CharField(max_length=20, default="", null=True, blank=True)
    description = models.CharField(max_length=20, default="", null=True, blank=True)
    amount = models.CharField(max_length=20, default="", null=True, blank=True)