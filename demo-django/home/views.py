from django.shortcuts import render

from .models import Mensagem


def index(request):
    mensagens = Mensagem.objects.filter(titulo__icontains="oi")
    return render(request, "home/index.html", {"mensagens": mensagens})

def sobre_view(request):
    return render(request, "home/sobre.html")