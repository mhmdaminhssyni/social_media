import os
import csv
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    



#--------------------------------------------------------
# class PostListView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serialaizer_class = PostSerializer
    
    
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#----------------------------------------------------------------
# class PostListView(generics.GenericAPIView,
#                    mixins.CreateModelMixin,
#                    mixins.ListModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class PostDetailView(generics.GenericAPIView,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#---------------------------------------------------------------
# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# class PostDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serialaizer = PostSerializer(post)
#         return Response(serialaizer.data)
            
            
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serialaizer = PostSerializer(post, data=request.data)
#         if serialaizer.is_valid():
#             serialaizer.save()
#             return Response(serialaizer.data)
#         return Response(serialaizer.errors , status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
            
            
        