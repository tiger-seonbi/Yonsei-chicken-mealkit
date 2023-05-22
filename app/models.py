from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):

    department_name = models.CharField(max_length=50)
    def __str__(self):
        return self.department_name

class Person(models.Model):
    # 추가 필드 정의
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_info")
    nickname = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, related_name="uers_department")
    #count_chicken = models.ForeignKey(CountChicken, on_delete=models.CASCADE, null=True, related_name="uers_chickens")
    def __str__(self):
        return self.nickname
    
class CountChicken(models.Model):

    quantity = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_chicken")
    #department = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="Department_chicken", db_column="department")
    # quantity_of_department = models.PositiveIntegerField()

