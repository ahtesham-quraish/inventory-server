from django.contrib import admin
from account.models import Transaction,Bank
# Register your models here.
admin.site.register(Bank)
admin.site.register(Transaction)