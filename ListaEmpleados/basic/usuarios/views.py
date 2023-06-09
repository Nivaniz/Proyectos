from django.shortcuts import render
from .models import Usuario


# Create your views here.
def usuariolist(request):
    get_usuarios = Usuario.objects.all() # Traemos toda la data de la clase usuarios
    data = {
        'get_usuarios': get_usuarios
    }
    return render(request, 'usuariolist.html', data)
