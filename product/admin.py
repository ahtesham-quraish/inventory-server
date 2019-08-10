from django.contrib import admin
from product.models import Product
from invoicce.models import Invoice, InvoiceItems
from customer.models import Customer
# Register your models here.

admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Customer)
admin.site.register(InvoiceItems)