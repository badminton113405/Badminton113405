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
]