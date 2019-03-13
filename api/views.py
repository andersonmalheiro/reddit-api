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
