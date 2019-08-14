from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from authentication.models import InstaUser
from users.models import UserConnection

class Post(models.Model):
    author = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='my_posts'
    )
    title = models.TextField(blank = True,null = True)
    # or models.ImageField()
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
    )


    # def get_absolute_url(self):
    #     return reverse('posts')
        # return reverse('detail', args = [str(self.id)])

    
    
