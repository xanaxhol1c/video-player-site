import os
from django.db import models

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
    image = models.ImageField(upload_to=images_upload_to)
    video = models.FileField(upload_to=videos_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return str(self.name)
