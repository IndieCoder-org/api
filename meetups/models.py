from django.db import models

# Create your models here.
class MeetUp(models.Model):
    title = models.CharField(max_length=30)
    where = models.CharField(max_length=20)
    when = models.DateTimeField()
    description = models.TextField()
    url = models.URLField()