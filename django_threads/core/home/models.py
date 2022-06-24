from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.student_name
