from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profile_pics',
        format = 'JPEG',
        options = {'quality':100},
        null = True,
        blank = True,
    )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

