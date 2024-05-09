# badminton_app/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    # 其他字段定义
