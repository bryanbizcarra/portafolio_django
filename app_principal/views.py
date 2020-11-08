from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app_principal.models import informacion_personal, conocimientos, trayectoria_laboral, trayectoria_academica


def index(request):
    mostrar_info_personal = informacion_personal.objects.all()
    mostrar_conocimientos = conocimientos.objects.all()
    mostrar_info_laboral = trayectoria_laboral.objects.all()
    mostrar_info_academica = trayectoria_academica.objects.all()
    context = {'informacion': mostrar_info_personal, 'conocimiento': mostrar_conocimientos, 'laboral': mostrar_info_laboral, 'academico': mostrar_info_academica}
    return render(request, 'index.html', context)


  