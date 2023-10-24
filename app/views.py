from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado,Entidad
# Create your views here.

def home(request):
    titulo="SIN"
    ordenado=Comunicado.objects.all().order_by('-fecha_publicacion')
    entidades=Entidad.objects.all()
    entidadselec = (request.GET.get("filtroentidades"))
    

    if entidadselec == 'Todos' or entidadselec is None:
        comunicados = Comunicado.objects.all()
    else:
        entidadfiltro = Entidad.objects.get(nombre=entidadselec)
        comunicados = Comunicado.objects.filter(entidad=entidadfiltro)
    comunicados = comunicados.order_by('-fecha_publicacion')


    data={"titulo":titulo,
          "comunicados":comunicados,
          "entidades":entidades,
          "ordenado":ordenado,
          "entidadselec":entidadselec,
          }
    return render(request, 'app/home.html', data)



