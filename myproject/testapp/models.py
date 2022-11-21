from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Tweet(models.Model):
    tweet = models.TextField()
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user')

    def __unicode__(self):
        return self.tweet

class User(AbstractUser):
    tweet = models.ManyToManyField(Tweet, blank=True)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

