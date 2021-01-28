from django.db import models

from django.utils import timezone


# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100000)
    pub_date = models.DateTimeField('publishing date', default=timezone.now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    pub_date = models.DateTimeField('publishing date', default=timezone.now())
    

    def __str__(self):
        return self.body