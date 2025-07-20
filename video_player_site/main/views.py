from django.shortcuts import render
from videos.models import Video
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    videos = Video.objects.all()
    paginator = Paginator(videos, 3)
    
    current_page = paginator.page((int(page)))
    return render(request, 'main/index.html', {'videos' : current_page})