from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Blog, Subscriber, Basket
from api.serializer import BlogGetSerializer, BlogPostSerializer, SubscriberSerializer, BasketSerializer


class BlogView(APIView):

    def get(self, request):
        blog = Blog.objects.filter(is_published=True)
        serializer = BlogGetSerializer(blog, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = BlogPostSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BlogDetailApiView(APIView):

    def get(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
            serializer = BlogGetSerializer(blog, context ={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND, data={'message': 'Blog not found'})
        

    def put(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
            serializer = BlogPostSerializer(blog, data=request.data, context={'request' : request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND, data={'message': 'Blog not found'})
        

    def delete(self, request, id):
        try:
             blog = Blog.objects.get(id=id)
             blog.delete()
             return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'Blog deletedl'})
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Blog not found'})
        


class SubsciberApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class SubscriberAPIView(APIView):
    
#     def get(self, request, *args, **kwargs):
#         sub = Subscriber.objects.all()
#         serializer = SubscriberSerializer(sub, many=True, context={'request': request})
#         return Response(data=serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = SubscriberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BasketApiView(APIView):
    
    def post(self, request, *args, **kwargs):
        user = request.user
        serizaler = BasketSerializer(data=request.data, context={'user': user})
        if serizaler.is_valid():
            serizaler.save()
            return Response(serizaler.data, status=status.HTTP_201_CREATED)
        return Response(serizaler.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get (self, request, *args, **kwargs):
        baskets = Basket.objects.filter(user=request.user)
        serializer = BasketSerializer(baskets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


