from django.urls import path

from .views import (PostCreateListAPIView, 
                    PostDetailView, 
                    CommentListView, 
                    CommentDetailView)


urlpatterns = [
    path("", PostCreateListAPIView.as_view()),
    path("<int:pk>/", PostDetailView.as_view()),
    path("<int:pk>/comments/", CommentListView.as_view()),
    path("<int:post_pk>/comments/<int:comment_pk>", CommentDetailView.as_view()),
]
