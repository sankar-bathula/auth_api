from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)
    def __str__(self):
        return self.ename
# class Student(models.Model):
#     sno=models.IntegerField()
#     sname=models.CharField(max_length=64)
#     smarks=models.IntegerField()
#     saddr=models.CharField(max_length=64)
#     def __str__(self):
#         return self.sno
# Create your models here.

# Create your models here.
