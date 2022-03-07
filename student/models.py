from django.db import models

# Create your models here.
class Position(models.Model):
    stack=models.CharField(max_length=100)


class Student(models.Model):
    fullname=models.CharField(max_length=100)
    students_code=models.CharField(max_length=4)
    mobile=models.CharField(max_length=15)
    sd=models.CharField(max_length=10)
    stack=models.ForeignKey(Position, on_delete=models.CASCADE)
