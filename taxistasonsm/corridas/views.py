#coding:utf-8
from django.shortcuts import render, get_object_or_404
from corridas.models import Corrida
from django.views.generic import CreateView
# Create your views here.

def corridas(request):
	corridas = Corrida.objects.all()
	return render(request, 'corridas.html', {'lista_corridas': corridas})

def corrida(request, id = None):
	corrida = get_object_or_404(Corrida, id=id)
	return render(request, 'corrida.html', {'corrida': corrida})
	
class CriarCorrida(CreateView):
    model = Corrida
    fields = '__all__'
    template_name = 'criar-corrida.html'
    success_url = '.'