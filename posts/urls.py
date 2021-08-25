from django.urls import path
from .views import (PostCreateListAPIView, 
                    PostDetailView, 
                    post_up_votes,
                    CommentListView, 
                    CommentDetailView,
                    ReplyListView,
                    ReplyDetailView)


urlpatterns = [
    path("", PostCreateListAPIView.as_view()),
    path("<int:pk>/<slug:slug>/", PostDetailView.as_view()),
    path("<int:pk>/", post_up_votes),
    path("<int:pk>/<slug:slug>/comments/", CommentListView.as_view()),
    path("<int:post_pk>/<slug:slug>/comments/<int:comment_pk>/", CommentDetailView.as_view()),
    path("<int:post_pk>/<slug:slug>/comments/<int:comment_pk>/replies/", ReplyListView.as_view()),
    path("<int:post_pk>/<slug:slug>/comments/<int:comment_pk>/replies/<int:reply_pk>/", ReplyDetailView.as_view()),
]
