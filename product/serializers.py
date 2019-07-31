from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Product
        fields = ('id','title','description', 'size','brand', 'unit', 'quatity','price','sae','api' ,'owner', 'created', 'updated')


class TopicRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Product.objects.all()

    def to_representation(self, value):

        topic = Product.objects.get(pk=value.pk)

        return {'pk': value.pk, 'text': topic.title}