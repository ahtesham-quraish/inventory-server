from django.contrib import admin
from account.models import Bank
from transaction.models import Transaction
# Register your models here.
admin.site.register(Bank)
admin.site.register(Transaction)