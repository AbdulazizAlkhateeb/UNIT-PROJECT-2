from django import forms
from .models import Teacher, Classroom, Course, ClassroomCourse

class TeacherForm(forms.ModelForm):
    class Meta:
        model  = Teacher
        fields = '__all__'

class ClassroomForm(forms.ModelForm):
    class Meta:
        model  = Classroom
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model  = Course
        fields = '__all__'


