from hello_world.models import Grettings
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    #CREANDO UN SALUDO
    greeting = Grettings()
    greeting.heading="hello world"
    greeting.save()

    #OBTENIENDO TODOS LOS SALUDOS
    greetings = Grettings.objects.all

    return render(request, 'index.html', {"greetings":greetings})