from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Registration, CourseType, CourseSession, Coach, DiscussionPost, DiscussionComment, CourseRegistration, Order, Product

# 自定義UserAdmin
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

# Registration管理
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'age', 'preferred_course', 'preferred_skill', 'gender')
    search_fields = ('name', 'email', 'preferred_course', 'preferred_skill')

admin.site.register(Registration, RegistrationAdmin)

# CourseType管理
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  
    search_fields = ('name',)  
    filter_horizontal = ('coaches',)  

# 註冊 CourseType 模型到管理後台
admin.site.register(CourseType, CourseTypeAdmin)

# CourseSession管理
class CourseSessionAdmin(admin.ModelAdmin):
    list_display = ('course_type', 'start_time', 'end_time', 'instructor', 'day_of_week')
    search_fields = ('course_type__name', 'instructor', 'day_of_week')

admin.site.register(CourseSession, CourseSessionAdmin)

# Coach管理
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'specialization', 'experience', 'contact_number')
    search_fields = ('name', 'specialization')

admin.site.register(Coach, CoachAdmin)

# DiscussionPost管理
class DiscussionPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    search_fields = ('author__username', 'content')

admin.site.register(DiscussionPost, DiscussionPostAdmin)

# DiscussionComment管理
class DiscussionCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('post__content', 'author__username', 'content')

admin.site.register(DiscussionComment, DiscussionCommentAdmin)

# CourseRegistration管理
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_type', 'sub_course_type', 'registration_date', 'cost')
    search_fields = ('user__username', 'course_type', 'sub_course_type')

admin.site.register(CourseRegistration, CourseRegistrationAdmin)

# Order管理
class OrderAdmin(admin.ModelAdmin):
    list_display = ('payer_name', 'payer_phone', 'payer_email', 'total_amount', 'created_at', 'paid')
    search_fields = ('payer_name', 'payer_phone', 'payer_email')
    list_filter = ('paid',)

admin.site.register(Order, OrderAdmin)

# Product管理
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

# 自定義後台頁面標題和標題欄自
admin.site.site_header = '羽你動資動' 
admin.site.site_title = '羽你動資動'   
admin.site.index_title = '羽你動資動管理'
