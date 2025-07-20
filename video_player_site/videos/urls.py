from django.urls import path
from .views import video_details, like_video

app_name = 'videos'

urlpatterns = [
    path('like/', like_video, name='like_video'),
    path('<slug:slug>/', video_details, name="video_details"),
    # path('stream/<int:video_id>', stream_video, name="stream_video"),
]
