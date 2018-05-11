from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context


# Create your views here.


def index(request, peticion_id):

    try:
        solicitud = Pages.objects.get(id=int(peticion_id))
        #en vez del id lo podemos hacer tambien con el nombre pero esta mejor asi
    except Pages.DoesNotExist:
        return HttpResponse('Page Not Found')
    respuesta = 'Hola, soy ' + solicitud.name + ": " + str(solicitud.page)
    return HttpResponse(respuesta)

@csrf_exempt
def paginanueva(request, nombre, pagina):
    if request.method == "GET":
        p = Pages(name=nombre, page=pagina)
        p.save()
    elif request.method == "PUT":  #cuando haga el put con poster acordarme de poner la barra al final que me ha dado ya error 4 veces
        if request.user.is_authenticated():
            info = request.body
            p = Pages(name=nombre, page=info)
            p.save()
            respuesta = 'Todo ha ido bien'
        else:
            respuesta = 'El usuario no esta autenticado'
    return HttpResponse(respuesta)

def dame_paginas(request):

    if request.user.is_authenticated():
        respuesta1 = 'Logged in as ' + request.user.username + ' .' + '<a href="/logout">Logout</a>'
    else:
        respuesta1 = 'Not logged in.' + ' <a href="/login">Login</a>'


    lista_paginas = Pages.objects.all()
    respuesta2 = "<ol>"
    for pag in lista_paginas:
        respuesta2 += '<li><a href="/cmsusersput/' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta2 += "</ol>"
    return HttpResponse(respuesta1 + respuesta2)


def usuario(request):
    respuesta = "Eres " + request.user.username
    return HttpResponse(respuesta)
