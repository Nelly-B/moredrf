from django.shortcuts import render
from .serializers import Postserailizer
from .models import Post
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
#  api view decorator
from rest_framework.response import Response
from rest_framework.decorators import api_view
# class based view
from rest_framework.views import APIView
from django.http import Http404
# Using generics and mixins
from rest_framework import generics, mixins

# Authentications
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#viewSet
from rest_framework import viewsets

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = Postserailizer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = Postserailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = Postserailizer
    queryset = Post.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id = None):
        return self.update(request)
    
    def delete(self, request, id = None):
        return self.destroy(request)
    
#///////////////////////////////////////////////////////////

class PostsAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = Postserailizer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Postserailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class postDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)

        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk): 
        post = self.get_object(pk)
        serializer = Postserailizer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = Postserailizer(post, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#///////////////////////////////////////////////////////////////////


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
        