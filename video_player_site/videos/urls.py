from django.urls import path
from .views import video_details

app_name = 'videos'

urlpatterns = [
    path('<slug:slug>/', video_details, name="video_details"),
    # path('stream/<int:video_id>', stream_video, name="stream_video"),
]
