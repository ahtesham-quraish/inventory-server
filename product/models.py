from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, default='N/A', null=True, blank=True)
    brand  = models.CharField(max_length=20)
    quatity  =models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20, default='')
    sae = models.CharField(max_length=20, default='')
    api = models.CharField(max_length=20, default='')
    unit = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title