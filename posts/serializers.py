from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, Comment, Reply


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    def validate_date(self, value):
        if self.instance and self.instance.date != value:
            raise ValidationError("You may not edit date!")
        return value

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'up_votes',
            'owner',
            'format_created_at',
            'format_updated_at',
            'get_absolute_url',
            'image',
            'get_image',
            'get_thumbnail',
        ]
        read_only_fields = ['owner', 'up_votes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'post_field',
            'content',
            'up_votes',
            'format_created_at'
        ]
        read_only_fields = [
            'owner',
            'post_field'
        ]


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            'id',
            'comment_field',
            'content',
            'up_votes',
            'format_created_at'
        ]
        read_only_fields = [
            'owner',
            'comment_field'
        ]
