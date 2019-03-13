from django.shortcuts import render
from api.models import Subreddit, Post, Comment
from api.serializers import SubredditSerializer, CommentSerializer, PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class SubredditList(APIView):
    def get(self, request):
        subreddits = Subreddit.objects.all()
        serializer = SubredditSerializer(subreddits, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubredditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubredditDetail(APIView):
    def get_object(self, id):
        try:
            return Subreddit.objects.get(pk=id)
        except Subreddit.DoesNotExist:
            raise Http404

    def get(self, request, id):
        subreddit = self.get_object(id)
        serializer = SubredditSerializer(subreddit)
        return Response(serializer.data)

    def put(self, request, id):
        subreddit = self.get_object(id)
        serializer = SubredditSerializer(
            subreddit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        subreddit = self.get_object(id)
        subreddit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(APIView):
    # Posts de um subreddit
    def get(self, request, id):
        posts = Post.objects.filter(subreddit=id)
        if 'order_by' in request.query_params:
            posts = posts.order_by(request.query_params['order_by'])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAll(APIView):
    # Todos os posts
    def get(self, request):
        posts = Post.objects.all()
        if 'order_by' in request.query_params:
            posts = posts.order_by(request.query_params['order_by'])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
