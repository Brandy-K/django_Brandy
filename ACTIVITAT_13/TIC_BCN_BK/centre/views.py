from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader


students_list = [
    {"id": 1, "name": "Brandy", "surname1": "Kisia", "surname2": "Kisia", "email": "2023_brandy.sherile@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 2, "name": "Natalia", "surname1": "Casanellas", "surname2": "Blanquer", "email": "2023_natalia.casanellas@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 3, "name": "Albert", "surname1": "Penades", "surname2": "Casajus", "email": "2023_albert.penades@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 4, "name": "Felix", "surname1": "Balbin", "surname2": "Silva", "email": "2023_felix.balbin@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 5, "name": "Adrian", "surname1": "Navarro", "surname2": "Perez", "email": "2023_adrian.navarro@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 6, "name": "Xavi", "surname1": "Porras", "surname2": "del Pino", "email": "2023_xavi.porras@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 7, "name": "Javier", "surname1": "Gimenez", "surname2": "Sanchez", "email": "2023_javier.gimenez@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 8, "name": "Daniel", "surname1": "Vallespin", "surname2": "Mellado", "email": "2023_daniel.vallespin@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 9, "name": "Victor Andres", "surname1": "Fernandez", "surname2": "Alvarez", "email": "2023_victor.fernandez@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]},
    {"id": 10, "name": "Iris", "surname1": "Vilaseca", "surname2": "Saenz", "email": "2023_iris.vilaseca@iticbcn.cat", "course": "daw", "module": ["M06", "M07", "M08"]}
]

teachers_list = [
    {"id": 1, "nom": "Roger", "cognom": "Sobrino", "edat": 39, "rol": "teacher", "curs": "DAM2B, DAW2A"},
    {"id": 2, "nom": "Josep", "cognom": "Oriol Roca", "edat": 25, "rol": "teacher", "curs": "DAM2B, DAW2A, DAW1A"},
    {"id": 3, "nom": "Juanma", "cognom": "Biel", "edat": 24, "rol": "teacher", "curs": "DAW2A, DAW2B"}
]

# View details of all students


def students(request):
    template = loader.get_template('students.html')
    context = {'students': students_list}
    dades = template.render(context)
    return HttpResponse(dades)

# View details of a single student (Fixed "unresolved reference")


def student_detail(request, pk):
    student_obj = next((s for s in students_list if s["id"] == pk), None)

    if student_obj is None:
        raise Http404("Student not found")

    return render(request, 'student_detail.html', {'student': student_obj})

# View details of all teachers


def teachers(request):
    template = loader.get_template('teachers.html')
    context = {'teachers': teachers_list}
    dades_teachers = template.render(context)
    return HttpResponse(dades_teachers)

# View  details of a single teacher


def teacher_detail(request, pk):
    teacher_obj = next((s for s in teachers_list if s["id"] == pk), None)

    if teacher_obj is None:
        raise Http404("Teacher not found")

    return render(request, 'teacher_detail.html', {'teacher': teacher_obj})
