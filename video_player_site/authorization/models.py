from django.db import models
from django.contrib.auth.models import AbstractUser
from videos.models import Video
# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

class UserModel(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.role is None:
            try:
                role = Role.objects.get(name='User')
                self.role = role
            except Role.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class UserLikes(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    like = models.BooleanField(default=None, null=True)

    class Meta:
        unique_together = ('user', 'video')
    
    
class UserRoleRequest(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    is_approved = models.BooleanField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Role Request"
        verbose_name_plural="Role Requests"


    def __str__(self):
        return str(f'{self.user.username} -> {self.role.name}')

