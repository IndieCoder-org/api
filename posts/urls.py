from django.urls import path

from .views import (
    PostCreateListAPIView,
    PostDetailView,
    post_up_votes,
)

urlpatterns = [
    path("", PostCreateListAPIView.as_view()),
    path("<int:pk>/<slug:slug>/", PostDetailView.as_view()),
    path("<int:pk>/", post_up_votes),
]
