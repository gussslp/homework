from django.db import models
from django.utils import timezone

class Yt_video(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"
