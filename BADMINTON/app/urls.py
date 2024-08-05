from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
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
    #------------
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('member_center/', views.member_center, name='member_center'),
    path('edit_member/', views.edit_member, name='edit_member'),
    path('member_redirect', views.member_redirect, name='member_redirect'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    #------------
    path('community/', views.community, name='community'),
    path('mall/', views.mall, name='mall'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
]
