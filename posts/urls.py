from django.urls import path

from .views import PostCreateListAPIView

urlpatterns = [
    path("", PostCreateListAPIView.as_view())
]
