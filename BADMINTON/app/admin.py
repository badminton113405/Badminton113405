from django.contrib import admin
from .models import User, Registration, CourseType, CourseSession, Coach, DiscussionPost, DiscussionComment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname', 'phone' , 'birth_date', 'gender')
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email'),
        }),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'age', 'preferred_course', 'preferred_skill', 'gender')
    search_fields = ('name', 'email', 'preferred_course')

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class CourseSessionAdmin(admin.ModelAdmin):
    list_display = ('course_type', 'start_time', 'end_time', 'instructor', 'day_of_week')
    search_fields = ('course_type__name', 'instructor', 'day_of_week')

class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'specialization', 'contact_number')
    search_fields = ('name', 'specialization')

class DiscussionPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    search_fields = ('author__username', 'content')
    list_filter = ('created_at',)

class DiscussionCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('post__content', 'author__username', 'content')
    list_filter = ('created_at',)