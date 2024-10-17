from django.http import HttpResponse

def saludo(rquest):
    return HttpResponse("Bienvenidos alumnos a nuestra primera sesion en Django")