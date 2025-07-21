import os
from django.db import models
from django.urls import reverse
from django.conf import settings
from cloudinary.models import CloudinaryField


def images_upload_to(instance, filename):
    category_slug = instance.category.slug if instance.category else 'uncategorized'
    return os.path.join('images', category_slug, filename)

def videos_upload_to(instance, filename):
    category_slug = instance.category.slug if instance.category else 'uncategorized'
    return os.path.join('videos', category_slug, filename)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)

class Video(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=400)
    image = CloudinaryField('image', resource_type='image')
    video = CloudinaryField('video', resource_type='video')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("videos:video_details", args=[self.slug])
    
    def get_streaming_src(self):
        path = str(self.video)
        public_id = path.split('/')[-1].split('.')[0]
        return f"https://player.cloudinary.com/embed/?cloud_name={settings.CLOUD_NAME}&public_id={public_id}&profile=cld-default"
    
