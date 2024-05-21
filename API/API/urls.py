from django.contrib import admin
from django.urls import path, include
from APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('APP.urls')),  # API 路由
    path('api/register_member/', views.register_member),
    path('api/create_message/', views.create_message),
    path('test', views.test)
]
