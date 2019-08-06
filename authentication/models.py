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

