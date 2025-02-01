from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students_list'),  # List of students
    path('students/<int:pk>/', views.student_detail, name='student_detail'),  # Individual student details

    path('teachers/', views.teachers, name='teachers_list'),  # List of teachers
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),  # Individual teacher details
]
