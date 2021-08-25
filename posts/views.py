from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from django.db.models import Q

from .serializers import PostSerializer, CommentSerializer, ReplySerializer
from .models import Post, Comment, Reply
from .permissions import IsOwner


""" METHODS:
    GET ---> /posts/, with 3 optional params (status, search, count)
    POST --> /posts/, POST new post
"""


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


""" METHODS:
    GET --> /posts/id/slug/, Post Details
    PUT --> /posts/id/slug/, Post Update
    DELETE --> /posts/id/slug/, Post Delete
"""


class PostDetailView(APIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, pk, slug, format=None):
        post = Post.objects.get(pk=pk, slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, slug, format=None):
        post = Post.objects.get(pk=pk, slug=slug)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, slug, format=None):
        post = Post.objects.get(pk=pk, slug=slug)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListView(APIView):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, pk, slug, format=None):
        post = Post.objects.get(pk=pk, slug=slug)
        comments = Comment.objects.filter(post_field=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentDetailView(APIView):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, post_pk, slug, comment_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_pk, slug, comment_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, slug, comment_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReplyListView(APIView):

    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, post_pk, slug, comment_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        replies = Reply.objects.filter(comment_field=comment)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

class ReplyDetailView(APIView):

    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get(self, request, post_pk, slug, comment_pk, reply_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        reply = Reply.objects.get(pk=reply_pk, comment_field=comment)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)

    def put(self, request, post_pk, slug, comment_pk, reply_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        reply = Reply.objects.get(pk=reply_pk, comment_field=comment)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_pk, slug, comment_pk, reply_pk, format=None):
        post = Post.objects.get(pk=post_pk, slug=slug)
        comment = Comment.objects.get(pk=comment_pk, post_field=post)
        reply = Reply.objects.get(pk=reply_pk, comment_field=comment)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" METHODS:
    POST --> /posts/id/, Post up_votes
"""


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_up_votes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.up_votes += 1
    post.save()
    data = {
        'success': True
    }
    return Response(data)
