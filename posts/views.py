from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import permissions

from django.db.models import Q

from .serializers import PostSerializer
from .models import Post
from .permissions import IsOwner


class PostCreateListAPIView(CreateModelMixin, ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self, *args, **kwargs):
        status = self.request.GET.get("status", None)
        search_txt = self.request.GET.get("search", "")
        count = self.request.GET.get("count", None)
        qs = super().get_queryset()
        if status:
            qs = qs.filter(status=status)
        if search_txt:
            query = Q(title__icontains=search_txt) | Q(content__icontains=search_txt)
            qs = qs.filter(query)
        try:
            count = int(count)
            qs = qs[:count]
        except (ValueError, TypeError):
            pass
        return qs

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
