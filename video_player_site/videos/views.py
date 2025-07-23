from django.shortcuts import render, get_object_or_404
from .models import Video
from authorization.models import UserLikes
from django.db.models import Case, When, Value, IntegerField
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from django.core.cache import cache
from django.db.models import F

# Create your views here.
def video_details(request, slug=None):
    video = get_object_or_404(Video, slug=slug, is_published=True)

    if request.user.is_authenticated:
        key = f'view:{request.user}:{video.id}'

        if not cache.get(key):
            Video.objects.filter(id=video.id).update(views=F('views') + 1)
            cache.set(key, 1, timeout=3600)


    category = video.category

    recommendations = Video.objects.filter(is_published=True).annotate(
        priority=Case(
            When(category=category, then=Value(0)),
            default=Value(1),
            output_field=IntegerField()
        )
    ).order_by('priority').exclude(name=video.name)[:4]
    return render(request, 'videos/video_details.html', {'video' : video, 'recommendations' : recommendations})

@login_required
@require_POST
def toggle_like(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    user = request.user

    like_obj, created = UserLikes.objects.get_or_create(user=user, video=video)

    if not created:
        like_obj.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked' : liked, 'likes' : video.userlikes_set.count()})

@login_required
def get_likes(request):
    user = request.user

    liked_videos = UserLikes.objects.filter(user=user).select_related('video')

    videos = []

    for like in liked_videos:
        if like.video.is_published == True:
            videos.append(like.video)
    
    return render(request, 'videos/liked_videos.html', {'videos' : videos})

    