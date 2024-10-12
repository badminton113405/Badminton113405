from django.urls import path
from . import views
from .views import payment

urlpatterns = [
    # 主頁
    path('', views.home, name='home'),

    # 課程頁面
    path('beginner/', views.beginner, name='beginner'),
    path('competitive/', views.competitive, name='competitive'),
    path('onetoone/', views.onetoone, name='onetoone'),
    path('zerodozen/', views.zerodozen, name='zerodozen'),
    path('summer/', views.summer, name='summer'),
    path('winter/', views.winter, name='winter'),

    # 教練頁面
    path('ZZT/', views.ZZT, name='ZZT'),
    path('CYZ/', views.CYZ, name='CYZ'),
    path('ZBY/', views.ZBY, name='ZBY'),
    path('HWH/', views.HWH, name='HWH'),

    # 特殊球類訓練頁面
    path('power_ball/', views.power_ball, name='power_ball'),
    path('left_right_ball/', views.left_right_ball, name='left_right_ball'),
    path('small_ball/', views.small_ball, name='small_ball'),

    # 用戶註冊與登錄
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('member_center/', views.member_center, name='member_center'),
    path('edit_member/', views.edit_member, name='edit_member'),
    path('member_redirect/', views.member_redirect, name='member_redirect'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('email-verification-sent/', views.email_verification_sent, name='email_verification_sent'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
    
    # 社群
    path('community/', views.community, name='community'),  
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),

    # 商城與購物車
    path('mall/', views.mall, name='mall'),
    path('payment/', views.payment, name='payment'),
    path('shopingcar/', views.shopingcar, name='shopingcar'),
    path('product01/', views.product01, name='product01'),
    path('product02/', views.product02, name='product02'),
    path('product03/', views.product03, name='product03'),
    path('product04/', views.product04, name='product04'),
    path('product05/', views.product05, name='product05'),
    path('product06/', views.product06, name='product06'),
    path('product07/', views.product07, name='product07'),
    path('product08/', views.product08, name='product08'),
    path('create_order/', views.create_order, name='create_order'),
    path('payment_success/<int:order_id>/', views.payment_success, name='payment_success'),
    path('products/', views.mall, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    # 課程報名與分析
    path('course_Registration/', views.course_Registration, name='course_Registration'),
    path('course_Analysis/', views.course_Analysis, name='course_Analysis'),
    path('course_Analysis_Registration/', views.course_Analysis_Registration, name='course_Analysis_Registration'),
    path('recommend/', views.recommend_teacher, name='recommend_teacher'),
    path('course_result/', views.course_result, name='course_result'),
    path('history/', views.registration_history, name='registration_history'),
    path('course_success/', views.course_success_page, name='course_success_page'),
]


