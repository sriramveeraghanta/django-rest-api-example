from django.shortcuts import render
from .models import Post

from rest_framework import serializers,viewsets, generics, mixins
# Create your views here.


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []


class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
