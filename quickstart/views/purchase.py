from quickstart.serializers.purchase import PurchaseSerializer
from quickstart.models.purchase import PurchaseModel
from rest_framework import generics, permissions # new

class PurchaseView(generics.ListCreateAPIView):
    queryset = PurchaseModel.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseModel.objects.all()
    serializer_class = PurchaseSerializer
