from django.db import models


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Classroom(models.Model):
#     name = models.CharField(max_length=50)
#     year = models.CharField(max_length=9)
#     section = models.CharField(max_length=30)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Classroom(models.Model):
    class GradeChoices(models.TextChoices):
        FIRST = "First Grade", "First Grade"
        SECOND = "Second Grade", "Second Grade"
        THIRD = "Third Grade", "Third Grade"
        FOURTH = "Fourth Grade", "Fourth Grade"
        FIFTH = "Fifth Grade", "Fifth Grade"
        SIXTH = "Sixth Grade", "Sixth Grade"

    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50, choices=GradeChoices.choices, default= "First Grade")
    section = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    class SemesterChoices(models.TextChoices):
        FIRST  = 'first',  'First Semester'
        SECOND = 'second', 'Second Semester'
        THIRD  = 'third',  'Third Semester'

    name = models.CharField(max_length=100)
    description = models.TextField()
    coures_Image = models.ImageField(upload_to="images/", default="images/default.jpg")
    grade_level = models.CharField(max_length=50)
    semester = models.CharField(max_length=50,choices=SemesterChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClassroomCourse(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
