from django.urls import path
from . import views

urlpatterns = [
    path('Student', views.students, name='students'),
    path('Teacher', views.teachers, name='teachers'),
]
