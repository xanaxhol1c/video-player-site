from django import forms
from django.contrib.auth.hashers import make_password
from .models import UserModel, UserRoleRequest

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user        
    
class CreateUserRoleRequest(forms.ModelForm):
    class Meta:
        model = UserRoleRequest
        fields = ['role', 'message']