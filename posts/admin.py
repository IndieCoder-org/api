from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'owner',
        'up_votes',
        'created_at',
    ]

admin.site.register(Comment)