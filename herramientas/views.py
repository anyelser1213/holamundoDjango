from django.shortcuts import render

# Create your views here.

def index(request):

    print("index de herramienta")
    return render(request, 'herramientas/index.html')
