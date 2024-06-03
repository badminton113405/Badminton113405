from django.urls import path
from .views import RegisterView, CustomLoginView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),  # 使用自定义登录视图
    path('profile/', UserDetailView.as_view(), name='profile'),
]
