from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .models import Student, Attendance, Classroom
from .forms import StudentForm, AttendanceForm
from datetime import date








# Create your views here.


# students_view
def students_view(request: HttpRequest):
    students = Student.objects.select_related("classroom").all()

    selected_classroom = request.GET.get("classroom")
    if selected_classroom:
        students = Student.objects.select_related("classroom").filter(classroom_id=selected_classroom)
    else:
        students = Student.objects.select_related("classroom").all()

    return render(request, "student/students.html", {"students": students, "classrooms": Classroom.objects.all()})


def create_student_view(request: HttpRequest):
    student_form = StudentForm()
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "Student added successfully.")
            return redirect("student:students_view")
        else:
            messages.error(request, "Form is not valid.")
    return redirect("student:students_view")



def update_student_view(request: HttpRequest, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, "Student updated.")
            return redirect("student:students_view")
        else:
            messages.error(request, "Form is not valid.")
    return render(request, "student/update_students.html", {"student": student, "classrooms": Classroom.objects.all()})



def delete_student_view(request: HttpRequest, student_id: int):
    student = Student.objects.get(pk=student_id)
    student.delete()
    messages.info(request, "Student deleted.")
    return redirect("student:students_view")







#attendance_view


def attendance_view(request: HttpRequest):
    classrooms = Classroom.objects.all()
    selected_classroom_id = request.GET.get("classroom")
    selected_date = request.GET.get("date") or date.today().isoformat()

    students = []
    if selected_classroom_id:
        students = Student.objects.filter(classroom_id=selected_classroom_id)

    if request.method == "POST":
        selected_classroom_id = request.POST.get("classroom_id")
        selected_date = request.POST.get("date") or date.today().isoformat()

        for student in Student.objects.filter(classroom_id=selected_classroom_id):
            status = request.POST.get(f"status_{student.id}")
            remark = request.POST.get(f"remark_{student.id}", "")

            Attendance.objects.update_or_create(
                student=student,
                date=selected_date,
                defaults={
                    "status": status,
                    "remark": remark,
                }
            )

        messages.success(request, "Attendance saved successfully.")
        return redirect("student:attendance_view")

    return render(request, "student/attendance.html", {
        "classrooms": classrooms,
        "students": students,
        "selected_classroom_id": selected_classroom_id,
        "selected_date": selected_date,
        "StatusChoices": Attendance.StatusChoices.choices,
    })




def student_attendance_history_view(request: HttpRequest, student_id: int):
    student = Student.objects.get(pk=student_id)
    attendance_records = Attendance.objects.filter(student=student).order_by("-date")

    return render(request, "student/student_attendance_history.html", {"student": student, "attendance_records": attendance_records})



def attendance_report_view(request: HttpRequest):
    classrooms = Classroom.objects.all()
    selected_classroom = request.GET.get("classroom")
    selected_date = request.GET.get("date")

    records = Attendance.objects.select_related("student").order_by("-date")

    if selected_classroom:
        records = records.filter(student__classroom_id=selected_classroom)

    if selected_date:
        records = records.filter(date=selected_date)

    return render(request, "student/attendance_report.html", {
        "records": records,
        "classrooms": classrooms,
        "selected_classroom": selected_classroom,
        "selected_date": selected_date,
    })