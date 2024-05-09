from rest_framework import serializers
from .models import MyModel  # 确保 MyModel 已定义在 models.py

# 使用 ModelSerializer
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel  # 绑定 Django 模型
        fields = '__all__'  # 序列化所有字段
