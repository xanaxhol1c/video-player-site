from django.shortcuts import render
from videos.models import Video

# Create your views here.
def index(request):
    videos = Video.objects.all()
    print(videos.first())
    return render(request, 'main/index.html', {'videos' : videos})