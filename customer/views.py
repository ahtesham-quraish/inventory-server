from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import generics, permissions # new

class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

