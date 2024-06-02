# API/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APP import views
from APP.views import MyModelViewSet, login, register

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', login, name='login'),
    path('api/register/', register, name='register'),
    path('', views.index, name='index'), 
]
