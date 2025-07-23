from django.urls import path
from .views import index, for_creators, upload_success, create_role_request

app_name="main"

urlpatterns = [
    path('', index, name='index'),
    path('for-creators/', for_creators, name='for_creators'),
    path('create-role-request/', create_role_request, name="create_role_request"),
    path('upload-success/', upload_success, name='upload_success'),
]
