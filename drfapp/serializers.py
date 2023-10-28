from rest_framework import serializers
from .models import Post
from rest_framework.serializers import ModelSerializer

class Postserailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        