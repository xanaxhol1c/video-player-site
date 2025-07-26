from django import forms
from videos.models import Video
from pytils.translit import slugify

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name',
                  'category',
                  'description',
                  'image',
                  'video']
    
    def save(self, commit=True):
        video = super().save(commit=False)
        video.slug = slugify(str(video.name))

        if commit:
            video.save()
        
        return video
