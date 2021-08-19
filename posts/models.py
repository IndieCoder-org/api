from io import BytesIO
from PIL import Image

from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from django.core.files import File


host_url = 'http://127.0.0.1:8000'


class CommonInfo(models.Model):
    """
        Model inheritance:
        pros: it easy to understand at first glance.
        cons: if there are a lot of fields duplicated, it would be hard to maintain
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def format_created_at(self):
        return self.created_at.strftime('%H:%M | %b %d, %Y')

    def format_updated_at(self):
        return self.updated_at.strftime('%H:%M | %b %d, %Y')


class Post(CommonInfo, models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='created_at')
    content = models.TextField()
    up_votes = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='uploads/posts/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def get_image(self):
        if self.image:
            return host_url + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return host_url + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return host_url + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(400, 225)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Comment(CommonInfo, models.Model):
    post_field = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    up_votes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"comment on - {self.post_field}"


class Reply(CommonInfo, models.Model):
    comment_field = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='+')
    content = models.TextField()
    up_votes = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Replies"

    def __str__(self):
        return f"reply to - {self.comment_field}"
