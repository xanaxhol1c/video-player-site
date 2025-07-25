from django.contrib import admin
from .models import Category, Video

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'description', 'image', 'video', 'created_at', 'is_published']
    list_filter = ['name', 'category', 'is_published', 'created_at']
    prepopulated_fields = {'slug' : ('name',)}
    readonly_fields = ['views']

    actions = ['approve_videos', 'hide_videos']

    def approve_videos(self, request, queryset):
        for video in queryset:
            if not video.is_published:
                video.is_published = True
                video.save()

    def hide_videos(self, request, queryset):
        for video in queryset:
            if video.is_published:
                video.is_published = False
                video.save()

    approve_videos.short_description = '✅ Approve selected videos'
    hide_videos.short_description = '❌ Hide selected videos'
