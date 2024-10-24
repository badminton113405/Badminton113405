from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Registration, CourseType, CourseSession, Coach, DiscussionPost, DiscussionComment, CourseRegistration, Order, Product

# UserAdmin
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('個人資訊', {'fields': ('full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email')}),
        ('權限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('重要日期', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'gender', 'birth_date', 'nickname', 'phone', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'full_name', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)

# Registration
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'age', 'preferred_course', 'preferred_skill', 'gender')
    search_fields = ('name', 'email', 'preferred_course', 'preferred_skill')

admin.site.register(Registration, RegistrationAdmin)

# CourseType
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  
    search_fields = ('name',)  
    filter_horizontal = ('coaches',)  

admin.site.register(CourseType, CourseTypeAdmin)

# CourseSession
class CourseSessionAdmin(admin.ModelAdmin):
    list_display = ('course_type', 'start_time', 'end_time', 'instructor', 'day_of_week')
    search_fields = ('course_type__name', 'instructor', 'day_of_week')

admin.site.register(CourseSession, CourseSessionAdmin)

# Coach
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'specialization', 'experience', 'contact_number')
    search_fields = ('name', 'specialization')

admin.site.register(Coach, CoachAdmin)

# DiscussionPost
class DiscussionPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    search_fields = ('author__username', 'content')

admin.site.register(DiscussionPost, DiscussionPostAdmin)

# DiscussionComment
class DiscussionCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('post__content', 'author__username', 'content')

admin.site.register(DiscussionComment, DiscussionCommentAdmin)

# CourseRegistration
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_type', 'sub_course_type', 'registration_date', 'cost')
    search_fields = ('user__username', 'course_type', 'sub_course_type')

admin.site.register(CourseRegistration, CourseRegistrationAdmin)

# Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('payer_name', 'payer_phone', 'payer_email', 'total_amount', 'created_at', 'paid')
    search_fields = ('payer_name', 'payer_phone', 'payer_email')
    list_filter = ('paid',)

admin.site.register(Order, OrderAdmin)

# Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

admin.site.site_header = '羽你動資動' 
admin.site.site_title = '羽你動資動'   
admin.site.index_title = '羽你動資動管理'
