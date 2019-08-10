from django.db import models
# from customer.models import Customer


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=20, default="", null=True, blank=True)
    code = models.CharField(max_length=20, default="", null=True, blank=True)
    entry_method = models.CharField(max_length=20, default="", null=True, blank=True)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, default="", null=True, blank=True)
    code = models.CharField(max_length=20, default="", null=True, blank=True)
    type = models.CharField(max_length=20, default="", null=True, blank=True)
    title = models.CharField(max_length=20, default="", null=True, blank=True)

