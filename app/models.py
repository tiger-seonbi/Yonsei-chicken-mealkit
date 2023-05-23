from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    # 추가 필드 정의
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Person')
    nickname = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    #count_chicken = models.ForeignKey(CountChicken, on_delete=models.CASCADE, null=True, related_name="uers_chickens")
    def __str__(self):
        return self.nickname
    
class CountChicken(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Count')
    quantity = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_chicken")
    department = models.CharField(max_length=50)
    # quantity_of_department = models.PositiveIntegerField()

