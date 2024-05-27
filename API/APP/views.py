# views.py
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from django.shortcuts import render
from django.http import HttpResponse

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

def login(request):
    return HttpResponse("Login view")

def register(request):
    return HttpResponse("Register view")

def index(request):
    return render(request, 'index.html')
