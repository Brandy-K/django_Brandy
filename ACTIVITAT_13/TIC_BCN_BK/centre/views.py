from django.shortcuts import render
from .models import Students, Teachers


# Create your views here.


def students(request):
    students = Students.objects.all()
    return render(request, 'templates/students.html', {'students': students})


def teachers(request):
    teachers = Teachers.objects.all()
    return render(request, 'templates/teachers.html', {'teachers': teachers})
