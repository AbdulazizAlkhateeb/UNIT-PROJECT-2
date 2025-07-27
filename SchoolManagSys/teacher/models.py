from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Classroom(models.Model):
    name = models.CharField(max_length=10)   
    year = models.CharField(max_length=9)   
    section = models.CharField(max_length=2)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    coures_Image = models.ImageField(upload_to="images/", default="images/default.jpg")
    grade_level = models.CharField(max_length=20)
    semester = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ClassroomCourse(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
