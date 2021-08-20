from django.contrib import admin
from .models import Post, Comment, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'owner',
        'up_votes',
        'created_at',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'content',
        'post_field',
        'owner',
        'created_at',
    ]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = [
        'content',
        'comment_field',
        'owner',
        'created_at',
    ]
