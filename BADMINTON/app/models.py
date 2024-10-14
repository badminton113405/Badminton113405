from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission,BaseUserManager
from django.conf import settings
from django.urls import reverse


class CourseRegistration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=100)
    sub_course_type = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('birth_date', '1900-01-01')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    birth_date = models.DateField()
    nickname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  
        blank=True
    )

    objects = UserManager() 

class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    preferred_course = models.CharField(max_length=100)
    preferred_skill = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    def __str__(self):
        return f"{self.name} - {self.preferred_course}"

class CourseType(models.Model):
    name = models.CharField(max_length=100)  # 班级名称
    applicable_level = models.CharField(max_length=100, blank=True, null=True)  # 适用阶级（选填）
    description = models.TextField(blank=True, null=True)  # 班级介绍 1
    additional_description_1 = models.TextField(blank=True, null=True)  # 班级介绍 2
    additional_description_2 = models.TextField(blank=True, null=True)  # 班级介绍 3
    price = models.DecimalField(max_digits=6, decimal_places=2)  # 价格
    image = models.ImageField(upload_to='courses/', blank=True, null=True)  # 照片
    coaches = models.ManyToManyField('Coach', blank=True)  # 指導教練
    slug = models.SlugField(unique=True, default='default-slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

class CourseSession(models.Model):
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instructor = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', '星期一'), 
        ('Tuesday', '星期二'), 
        ('Wednesday', '星期三'),
        ('Thursday', '星期四'),
        ('Friday', '星期五'),
        ('Saturday', '星期六'),
        ('Sunday', '星期日')
    ])

    def __str__(self):
        return f"{self.course_type.name} - {self.day_of_week}"

class Coach(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', '男'), ('female', '女'), ('other', '其他')])
    personal_traits = models.CharField(max_length=255, blank=True, null=True)  # 添加个人特质字段
    specialization = models.CharField(max_length=100)
    experience = models.TextField()
    teaching_method = models.TextField(blank=True, null=True)  # 添加教学方式字段
    contact_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='coaches/')
    slug = models.SlugField(unique=True, default='default-slug')  # 添加slug字段用于友好的URL

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coach_detail', kwargs={'slug': self.slug})

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
    
   
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payer_name = models.CharField(max_length=255)
    payer_phone = models.CharField(max_length=20)
    payer_email = models.EmailField()
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.payer_name} - {self.total_amount}"


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

