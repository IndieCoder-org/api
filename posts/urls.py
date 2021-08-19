from django.urls import path

from .views import PostCreateListAPIView, PostDetailView

urlpatterns = [
    path("", PostCreateListAPIView.as_view()),
    path("<int:pk>/", PostDetailView.as_view()),
]
