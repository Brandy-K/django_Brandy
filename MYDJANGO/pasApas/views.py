from django.shortcuts import render, redirect


# Create your views here.


def guardar_session(request):
    request.session['usuario'] = 'Juan'
    return render(request, 'guardar_session.html')


def recuperar_session(request):
    usuario = request.session.get('usuario','Invitado')
    return render(request, 'recuperar_session.html',{'usuario':usuario})


def eliminar_session(request):

    if 'usuario' in request.session:
        del request.session['usuario']
        return redirect('recuperar_session')
