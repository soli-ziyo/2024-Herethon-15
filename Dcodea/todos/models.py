from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 정보
    description = models.CharField(max_length=255, default='')  # 작업 설명
    date = models.DateField(default=timezone.now) # 작업 날짜
    
    def __str__(self):
        return f"{self.description} - {self.date}"