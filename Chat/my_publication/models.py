from django.db import models
from django.contrib.auth.models import User
"""
Склад моделі: 
🔘 Зв’язок User з User_Post
🔘 Назва публікації
🔘 Тема публікації 
🔘 Теги публікації: відпочинок, натхнення, життя, природа, читання, спокій, гармонія, музика, фільми, подорожі. Є можливість додати новий тег
🔘 Текст публікації
🔘 Посилання до цікавої статті (пруфи)
🔘 Зображення до публикації (максимум 9 до публікації)
🔘 Кількість переглядів публікації (один користувач один перегляд, навіть після повторного перегляду)
🔘 Кількість вподобайок
"""

# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length= 255)
class UserPostModel(models.Model):
    user = models.ForeignKey(to= User, on_delete= models.CASCADE, null= True)
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=150)
    tags = models.ForeignKey(to= TagModel, null= True, on_delete= models.DO_NOTHING)
    text = models.TextField()
    link = models.CharField(max_length=255)
    # image = models.ImageField()
    views = models.IntegerField(default= 0)
    like = models.IntegerField(default= 0)
    
    