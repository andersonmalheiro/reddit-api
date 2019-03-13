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
    """
    get:
    Return a subreddit.

    put:
    Update a subreddit.

    delete:
    Delete a subreddit.
    """
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


class PostsBySubreddit(APIView):
    """
    get:
    Return the list of posts of a subreddit.
    """
    def get(self, request, id):
        posts = Post.objects.filter(subreddit=id)
        if 'order_by' in request.query_params:
            posts = posts.order_by(request.query_params['order_by'])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostList(APIView):
    # Todos os posts
    def get(self, request):
        posts = Post.objects.all()
        if 'order_by' in request.query_params:
            posts = posts.order_by(request.query_params['order_by'])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get_object(self, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentsByPost(APIView):
    def get(self, request, id):
        comments = Comment.objects.filter(post=id)
        
        if 'order_by' in request.query_params:
            comments = comments.order_by(request.query_params['order_by'])

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()

        if 'order_by' in request.query_params:
            comments = comments.order_by(request.query_params['order_by'])

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        {
            "text": "teste de comentário",
            "author": "John",
            "post": 2,
        }
        """
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    def get_object(self, id):
        try:
            return Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = self.get_object(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)