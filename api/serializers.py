from rest_framework import serializers
from api.models import Subreddit, Post, Comment


class SubredditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subreddit
        fields = ['id', 'name', 'description', 'createdAt']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'subreddit',
                  'author', 'likes', 'dislikes', 'createdAt']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post',
                  'likes', 'dislikes', 'createdAt']
