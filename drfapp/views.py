from django.shortcuts import render
from .serializers import Postserailizer
from .models import Post
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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
    
@csrf_exempt
def post_details(request, pk):
    try:
        post = Post.objects.get(pk=pk)

    except post.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method  == 'GET':
        serializer = Postserailizer(post)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Postserailizer(post, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)
        