from quickstart.models.product import ProductModel
from quickstart.serializers.product import ProductSerializer
from rest_framework import generics, permissions # new

class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
