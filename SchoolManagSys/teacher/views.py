from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .models import Teacher, Classroom
from .forms import TeacherForm, ClassroomForm

# Create your views here.


# teachers_views
def teachers_view(request: HttpRequest):
    teachers = Teacher.objects.all()
    majors_count = Teacher.objects.values('major').distinct().count()
    return render(request, "teacher/teachers.html", {"teachers": teachers, 'majors_count': majors_count,})


def create_teacher_view(request: HttpRequest):
    teacher_form = TeacherForm()
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            messages.success(request, "Teacher created successfully.")
        else:
            messages.error(request, "Invalid form submission.")

    return redirect("teacher:teachers_view")



def delete_teacher_view(request: HttpRequest, teacher_pk: int):
    teacher = Teacher.objects.get(pk=teacher_pk)
    teacher.delete()
    messages.info(request, "Teacher removed.")
    return redirect("teacher:teachers_view")


def update_teacher_view(request: HttpRequest, teacher_id: int):
    teacher = Teacher.objects.get(pk=teacher_id)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated successfully.")
            return redirect("teacher:teachers_view")
        else:
            messages.error(request, "Form is not valid.")

    return render(request, "teacher/update_teacher.html", {"teacher": teacher})



# classrooms_view
def classrooms_view(request: HttpRequest):
    classrooms = Classroom.objects.all()
    return render(request, "teacher/classrooms.html", {"classrooms": classrooms})



def create_classroom_view(request: HttpRequest):
    classrooms_form = ClassroomForm()
    if request.method == "POST":
        classrooms_form = ClassroomForm(request.POST)
        if classrooms_form.is_valid():
            classrooms_form.save()
            messages.success(request, "Classroom created successfully.")
            return redirect("teacher:classrooms_view")
        else:
            messages.error(request, "Invalid form data.")
 
    return redirect("teacher:classrooms_view")



def delete_classroom_view(request, classroom_id: int ):
    classroom = Classroom.objects.get(pk=classroom_id)
    classroom.delete()
    messages.info(request, "Classroom deleted.")
    return redirect("teacher:classrooms_view")


def update_classroom_view(request: HttpRequest, classroom_id: int):
    classroom = Classroom.objects.get(pk=classroom_id)

    if request.method == "POST":
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, "Classroom updated successfully.")
            return redirect("teacher:classrooms_view")
        else:
            messages.error(request, "Invalid form data.")

    return render(request, "teacher/update_classroom.html", {"classroom": classroom})

