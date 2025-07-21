from django.urls import path
from .views import video_details, toggle_like

app_name = 'videos'

urlpatterns = [
    path('<int:video_id>/toggle_like/', toggle_like, name='toggle_like'),
    path('<slug:slug>/', video_details, name="video_details"),
    # path('stream/<int:video_id>', stream_video, name="stream_video"),
]
