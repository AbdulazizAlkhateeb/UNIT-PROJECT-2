from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from student.models import Student, Attendance
from teacher.models import Teacher, Classroom

# Create your views here.

def home_view(request: HttpRequest):
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    classroom_count = Classroom.objects.count()

    total_attendance = Attendance.objects.count()
    present_attendance = Attendance.objects.filter(status='present').count()
    attendance_rate = round((present_attendance / total_attendance) * 100, 1) if total_attendance > 0 else 0

    return render(request, "main/index.html", {"student_count": student_count, "teacher_count": teacher_count, "classroom_count": classroom_count, "attendance_rate": attendance_rate,})



def about_view(request: HttpRequest):
    return render(request, "main/about.html")