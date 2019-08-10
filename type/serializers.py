from rest_framework import serializers
from type.models import Type

class TypeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Type
        fields = ('type','sub_type')

