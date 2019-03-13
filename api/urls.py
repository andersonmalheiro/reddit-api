from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *

urlpatterns = [
    path('subreddits/', SubredditList.as_view()),
    path('subreddits/<int:id>/', SubredditDetail.as_view()),
    path('subreddits/<int:id>/posts/', PostsBySubreddit.as_view()),
    path('posts/', PostList.as_view()),
    path('posts/<int:id>/', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
