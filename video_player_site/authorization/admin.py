from django.contrib import admin
from .models import Role, UserModel

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']
    readonly_fields = ['password', 
                       'last_login', 
                       'is_superuser', 
                       'username',
                       'first_name',
                       'last_name',
                       'is_staff',
                       'is_active',
                       'date_joined',
                       'groups',
                       'email',
                       'user_permissions']
    
    def has_add_permission(self, request):
        return False