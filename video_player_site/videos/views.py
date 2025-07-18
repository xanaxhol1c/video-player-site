from django.shortcuts import render
from .models import Video
from .utils import open_file
from django.http import StreamingHttpResponse

# Create your views here.
def video_details(request, slug=None):
    video = Video.objects.filter(slug=slug).first()
    return render(request, 'videos/video_details.html', {'video' : video})

def stream_video(request, video_id):
    file, status_code, content_length, content_range = open_file(request, video_id)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response