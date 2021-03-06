from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from course.models import Course




class Nuser(AbstractUser):
    real_name = models.CharField(max_length=10,default="woods")
    sigh = models.CharField(max_length=100, default="I am good!")
    school = models.CharField(max_length=20, default="0")
    grade = models.IntegerField(default=2018)
    table_time = models.DateTimeField(auto_now_add=True)
    can_post = models.BooleanField(default=False)
    term = models.CharField(max_length=20, default="0")
    week = models.CharField(max_length=20, default="0")
    art = models.FloatField(default=0.0)
    communication = models.FloatField(default=0.0)
    society = models.FloatField(default=0.0)
    internation = models.FloatField(default=0.0)
    leader = models.FloatField(default=0.0)
    science = models.FloatField(default=0.0)
    logic = models.FloatField(default=0.0)
    others = models.FloatField(default=0.0)
    def __str__(self):
        return self.username

class CourseTable(models.Model):#课表
    # id = models.IntegerField(default=0,primary_key=True)
    user = models.ForeignKey(Nuser, on_delete=models.CASCADE)
    course_id = models.IntegerField()

    def __str__(self):
        return self.user.username

class Coursecolle(models.Model):#收藏的课表
    # id = models.IntegerField(default=0,primary_key=True)
    course_id = models.IntegerField()
    user = models.ForeignKey(Nuser, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Coursehistory(models.Model):#浏览过的课表
    # id = models.IntegerField(default=0,primary_key=True)
    user = models.ForeignKey(Nuser, on_delete=models.CASCADE)
    course_id = models.IntegerField()
    comment = models.CharField(max_length=200,default="写点什么吧！")

    def __str__(self):
        return self.user.username

