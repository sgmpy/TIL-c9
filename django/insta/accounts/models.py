from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    image = ProcessedImageField(
                    blank=True,
                    upload_to='profile/images', # 저장 위치
                    processors=[ResizeToFill(300,300)], # 처리할 작업 목록
                    format='JPEG', # 저장 포맷
                    options={'quality':90}, # 옵션
                )
                
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')