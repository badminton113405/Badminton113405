# badminton_app/views.py
from rest_framework import viewsets
from .models import MyModel  # 检查导入语句是否正确
from .serializers import MyModelSerializer  # 确保序列化器导入没有错误

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
