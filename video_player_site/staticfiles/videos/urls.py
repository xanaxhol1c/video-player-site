from django.urls import path
from .views import video_details, toggle_like, get_likes

app_name = 'videos'

urlpatterns = [
    path('likes/', get_likes, name="get_likes"),
    path('<int:video_id>/toggle_like/', toggle_like, name='toggle_like'),
    path('<slug:slug>/', video_details, name="video_details"),
    # path('stream/<int:video_id>', stream_video, name="stream_video"),
]
