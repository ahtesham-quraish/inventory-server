from django.db import models


class CustomerModel(models.Model):
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=20)
    Address1 = models.CharField(max_length=300)
    Address2 = models.CharField(max_length=300)
    Phone  = models.IntegerField()
    country  = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fName +" "+self.lName