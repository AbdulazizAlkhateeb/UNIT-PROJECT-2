from django import forms
from student.models import Student, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"


# class GradeForm(forms.ModelForm):
#     class Meta:
#         model = Grade
#         fields = "__all__"

