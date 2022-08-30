from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class CommentReply(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='user_replies', null=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies')
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='user_comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.content[:30]


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
