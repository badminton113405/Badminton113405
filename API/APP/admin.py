# APP/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()  # 移除 'groups' 和 'user_permissions'
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # 移除 'groups'

admin.site.register(User, UserAdmin)
