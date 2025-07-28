from django.urls import path
from . import views



app_name= "teacher"

urlpatterns= [
    path("", views.teachers_view, name="teachers_view"),
    path("new/", views.create_teacher_view, name="create_teacher_view"),
    path("<teacher_pk>/delete/", views.delete_teacher_view, name="delete_teacher_view"),
    path("<teacher_id>/edit/", views.update_teacher_view, name="update_teacher_view"),

    path("classrooms/", views.classrooms_view, name="classrooms_view"),
    path("classrooms/create/", views.create_classroom_view, name="create_classroom_view"),
    path("classrooms/delete/<classroom_id>/", views.delete_classroom_view, name="delete_classroom_view"),
    path("classrooms/update/<classroom_id>/", views.update_classroom_view, name="update_classroom_view"),

]

