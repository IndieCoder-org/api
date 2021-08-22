from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.PostCreateListAPIView.as_view()
    ),
    path(
        "<int:pk>/<slug:slug>/",
        views.PostDetailView.as_view()
    ),
    path(
        "<int:pk>/",
        views.post_up_votes
    ),
    path(
        "<int:pk>/<slug:slug>/comments/",
        views.CommentListView.as_view()
    ),
    path(
        "<int:post_pk>/<slug:slug>/comments/<int:comment_pk>/",
        views.CommentDetailView.as_view()
    ),
    path(
        "comments/<int:pk>/",
        views.comment_up_votes
    )
]
