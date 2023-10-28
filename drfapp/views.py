from django.shortcuts import render
from .serializers import Postserailizer
from .models import Post
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

def postsView(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = Postserailizer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Postserailizer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = 400)