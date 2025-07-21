from django.db import models
from django.contrib.auth.models import AbstractUser
from videos.models import Video
# Create your models here.
class UserModel(AbstractUser):
    pass

class UserLikes(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    like = models.BooleanField(default=None, null=True)

    class Meta:
        unique_together = ('user', 'video')
    
    