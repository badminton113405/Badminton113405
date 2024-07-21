from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('community-view/', views.community, name='community'),
    path('beginner-view/', views.beginner, name='beginner'),
    path('competitive-view/', views.competitive, name='competitive'),
    path('onetoone-view/', views.onetoone, name='onetoone'),
    path('zerodozen-view/', views.zerodozen, name='zerodozen'),
    path('ZZT/', views.ZZT, name='ZZT'),
    path('CYZ/', views.CYZ, name='CYZ'),
    path('ZBY/', views.ZBY, name='ZBY'),
    path('HWH/', views.HWH, name='HWH'),
    path('power_ball',views.power_ball, name='power_ball'),
    path('left_right_ball',views.left_right_ball, name='left_right_ball'),
    path('small_ball',views.small_ball, name='small_ball'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('member_center/', views.member_center, name='member_center'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]