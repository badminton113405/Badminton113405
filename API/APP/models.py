from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email



class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


# Profile model to store additional information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    # Add any other fields you need

    def __str__(self):
        return self.user.email

class Member(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

class Message(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Coach(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

class Reservation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    reservation_date = models.DateField()


