from rest_framework import serializers
from quickstart.models import Todo

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username','email', 'snippets')

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # new
    class Meta:
        model = Todo

        fields = ('id','title', 'description','done', 'created', 'owner')