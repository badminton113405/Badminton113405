# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet, login, register, index

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),          # 包含 API 路由
    path('api/login/', login, name='login'),     # 登录 API 路由
    path('api/register/', register, name='register'), # 注册 API 路由
    path('', index, name='index'),               # Vue 应用入口
]
