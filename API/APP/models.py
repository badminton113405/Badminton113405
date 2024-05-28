from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='Default bio')  # 设置默认值
    avatar = models.ImageField(upload_to='avatars/', default='path/to/default/image.jpg')  # 设置默认值
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# 報名課程
class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    preferred_course = models.CharField(max_length=100)
    preferred_skill = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)


# 課程類型、時段
class CourseType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class CourseSession(models.Model):
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10)


# 教練
class Coach(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    specialization = models.CharField(max_length=100)
    experience = models.TextField()
    contact_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='instructors/')


# 留言板
class DiscussionPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class DiscussionComment(models.Model):
    post = models.ForeignKey(DiscussionPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
