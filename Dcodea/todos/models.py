from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 사용자 정보
    input_field  = models.CharField(max_length=255, default='')  # 작업 설명
    date = models.DateField(default=timezone.now) # 작업 날짜
    
    def __str__(self):
        return f"{self.description} - {self.date}"
    
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 사용자 정보
    introduction = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username