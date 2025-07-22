from .forms import UploadVideoForm
from functools import wraps
from django.shortcuts import render
from videos.models import Video, Category
from django.core.paginator import Paginator
from django.http.response import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def check_role(role_name):
    def wrapper(f):
        @wraps(f)
        def inner(request, *args, **kwargs):
            user = request.user

            try:
                if user.role.name != role_name:
                    return HttpResponseForbidden("Access denied")
            except AttributeError:
                return HttpResponseForbidden("Access denied")
            return f(request, *args, **kwargs)
        return inner
    return wrapper

def index(request):
    page = request.GET.get('page', 1)
    videos = Video.objects.all()
    paginator = Paginator(videos, 3)
    
    current_page = paginator.page((int(page)))
    return render(request, 'main/index.html', {'videos' : current_page})

@login_required
@check_role('Creator')
def for_creators(request):    
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            print('form saved successfully')
            #return redirect('main:upload_video_completed')

    else:
        form = UploadVideoForm()

    categories = Category.objects.all()

    return render(request, 'main/for_creators.html', {'categories' : categories, 'form' : form})