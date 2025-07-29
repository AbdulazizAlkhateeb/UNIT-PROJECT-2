from django.db import models
from teacher.models import Classroom, Course

# Create your models here.



class Student(models.Model):    
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Attendance(models.Model):
    class StatusChoices(models.TextChoices):
        PRESENT = 'present',   'Present'
        ABSENT  = 'absent',    'Absent'
        EXCUSED = 'excused',   'Excused'
        LATE    = 'late',      'Late'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default="present")
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)