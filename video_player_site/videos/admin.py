from django.contrib import admin
from .models import Category, Video

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'description', 'image', 'video', 'created_at']
    list_filter = ['name', 'category', 'created_at']
    prepopulated_fields = {'slug' : ('name',)}
    readonly_fields = ['views']
