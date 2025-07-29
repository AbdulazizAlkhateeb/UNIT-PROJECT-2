from django.urls import path
from . import views



app_name= "student"

urlpatterns= [
    path("", views.students_view, name="students_view"),
    path("create/", views.create_student_view, name="create_student_view"),
    path("update/<student_id>/", views.update_student_view, name="update_student_view"),
    path("delete/<student_id>/", views.delete_student_view, name="delete_student_view"),

    path("attendance/", views.attendance_view, name="attendance_view"),
    path("attendance/history/<student_id>/", views.student_attendance_history_view, name="student_attendance_history_view"),
    path("attendance/report/", views.attendance_report_view, name="attendance_report_view")
]
