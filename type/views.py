from type.models import Type
from type.serializers import TypeSerializer
from rest_framework import generics, permissions # new

class TypeView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


