from django.shortcuts import render, get_object_or_404
from .models import Video
from authorization.models import UserLikes
from django.db.models import Case, When, Value, IntegerField
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def video_details(request, slug=None):
    video = get_object_or_404(Video, slug=slug)

    category = video.category

    recommendations = Video.objects.annotate(
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
# def stream_video(request, video_id):
#     file, status_code, content_length, content_range = open_file(request, video_id)
#     response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

#     response['Accept-Ranges'] = 'bytes'
#     response['Content-Length'] = str(content_length)
#     response['Cache-Control'] = 'no-cache'
#     response['Content-Range'] = content_range
#     return response