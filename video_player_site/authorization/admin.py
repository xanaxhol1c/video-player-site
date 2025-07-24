from django.contrib import admin
from .models import Role, UserModel, UserRoleRequest, UserComments

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
    
@admin.register(UserRoleRequest)
class UserRoleRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'message', 'is_approved']
    list_filter = ['is_approved', 'role']
    actions = ['approve_requests', 'deny_requests']

    def approve_requests(self, request, queryset):
        for req in queryset:
            if req.is_approved == None:
                req.is_approved = True
                req.save()
                user = req.user 
                user.role = req.role
                user.save()
    
    def deny_requests(self, request, queryset):
        queryset.update(is_approved=False)

    approve_requests.short_description = "✅ Approve selected requests"
    deny_requests.short_description = "❌ Reject selected requests"

@admin.register(UserComments)
class UserCommentsAdmin(admin.ModelAdmin):
    list_display=['user', 'video', 'comment', 'created_at']