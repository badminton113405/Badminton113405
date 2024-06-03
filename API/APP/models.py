from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    nickname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # 自定义 related_name 以避免冲突
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # 自定义 related_name 以避免冲突
        blank=True
    )

# 報名課程
class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    preferred_course = models.CharField(max_length=100)
    preferred_skill = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.preferred_course}"

# 課程類型、時段
class CourseType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class CourseSession(models.Model):
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.course_type.name} - {self.day_of_week}"

# 教練
class Coach(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    specialization = models.CharField(max_length=100)
    experience = models.TextField()
    contact_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='instructors/')

    def __str__(self):
        return self.name

# 留言板
class DiscussionPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"

class DiscussionComment(models.Model):
    post = models.ForeignKey(DiscussionPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"
