from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

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
