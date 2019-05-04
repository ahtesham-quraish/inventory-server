from quickstart.models.customers import CustomerModel
from quickstart.serializers.customers import CustomerSerializer
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics, permissions # new

class CustomerView(generics.ListCreateAPIView):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
