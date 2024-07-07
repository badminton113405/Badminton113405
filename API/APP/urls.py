from django.urls import path
from .views import RegisterView, CustomLoginView, UserDetailView, UserInfoView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('api/user/', UserInfoView.as_view(), name='user-info'),
]
