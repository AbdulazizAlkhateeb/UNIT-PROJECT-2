from django import forms
from .models import Teacher, Classroom, ClassroomCourse

class TeacherForm(forms.ModelForm):
    class Meta:
        model  = Teacher
        fields = '__all__'

class ClassroomForm(forms.ModelForm):
    class Meta:
        model  = Classroom
        fields = '__all__'




