from functools import wraps
from .forms import UploadVideoForm
from authorization.forms import CreateUserRoleRequest
from authorization.models import Role
from django.shortcuts import render, redirect
from django.urls import reverse
from videos.models import Video, Category
from django.core.paginator import Paginator
from django.core.cache import caches
from django.http.response import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages

secondary_cache = caches['secondary']

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
    videos = Video.objects.filter(is_published=True)
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
            return redirect(reverse('main:upload_success'))

    else:
        form = UploadVideoForm()

    categories = Category.objects.all()

    return render(request, 'main/for_creators.html', {'categories' : categories, 'form' : form})

@login_required
@check_role('Creator')
def upload_success(request):
    return render(request, 'main/upload_succecc.html')

@login_required
def create_role_request(request):   
    if request.method == 'POST':
        key = f'{request.user.username}'
        
        if not secondary_cache.get(key):
            form = CreateUserRoleRequest(request.POST)

            if form.is_valid():
                role_request = form.save(commit=False)
                role_request.user = request.user

                role_request.save()

                secondary_cache.set(key, 1,timeout=86400)
                return redirect(reverse('main:index'))
        else:
            messages.error(request, 'You can send role request not much that once in 24 hours')
            return redirect(reverse('main:create_role_request'))

    form = CreateUserRoleRequest()

    # roles = Role.objects.all().exclude(name__in=[request.user.role, 'User'])
    roles = Role.objects.filter(name='Creator')

    return render(request, 'main/create_role_request.html', {'form' : form, 'roles' : roles})