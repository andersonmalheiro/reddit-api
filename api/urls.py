from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import SubredditList, SubredditDetail

urlpatterns = [
    path('subreddits/', SubredditList.as_view()),
    path('subreddits/<int:id>', SubredditDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
