from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APP import views
from APP.views import MyModelViewSet, login, register, forgot_password, reset_password

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', login, name='login'),
    path('api/register/', register, name='register'),
    path('api/forgot-password/', forgot_password, name='forgot-password'),
    path('api/reset-password/<uidb64>/<token>/', reset_password, name='reset-password-confirm'),
    path('', views.index, name='index'),
]
