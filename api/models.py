from django.db import models

# Create your models here.


class Subreddit(models.Model):
    name = models.CharField('Name', max_length=15, blank=False, null=False)
    description = models.CharField('Description', max_length=120)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Title', max_length=30,
                             blank=False, null=False)
    description = models.CharField(
        'Description', max_length=300, blank=False, null=False)
    subreddit = models.ForeignKey(
        Subreddit, on_delete=models.CASCADE, related_name='Subreddit')
    author = models.CharField('Author', max_length=15,
                              blank=False, null=False)
    likes = models.PositiveIntegerField('Likes', default=0)
    dislikes = models.PositiveIntegerField('Dislikes', default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField('Comment', max_length=200)
    author = models.CharField('Author', max_length=15,
                              blank=False, null=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='Post')
    likes = models.PositiveIntegerField('Likes', default=0)
    dislikes = models.PositiveIntegerField('Dislikes', default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
