from django.db import models
from product.models import Product
from customer.models import Customer

class Purchase(models.Model):
    order_id = models.IntegerField()
    description = models.CharField(max_length=300)
    currency_type = models.CharField(max_length=10)
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    converted_price = models.IntegerField()
    delivery_status = models.CharField(max_length=20, default='pending')
    delivery_date = models.DateField()
    unit_purchased = models.IntegerField()
    remarks = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)