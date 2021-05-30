#coding:utf-8
from django.shortcuts import render, get_object_or_404
from investimentos.models import Investimento
from django.views.generic import CreateView
from corridas.models import Corrida
# Create your views here.
def investimentos(request):
	investimentos = Investimento.objects.all()
	return render(request, 'investimentos.html', {'lista_investimentos': investimentos})
	
def investimento(request, id = None):
	investimento = get_object_or_404(Investimento, id=id)
	return render(request, 'investimento.html', {'investimento': investimento})
	
def lucro(request):
	investimentos = Investimento.objects.all()
	corridas = Corrida.objects.all()
	lucro = 0
	for investimento in investimentos:
		lucro = lucro - (investimento.combustivel*investimento.valor_combustivel)
		lucro = lucro - investimento.valor_IPVA
		lucro = lucro - investimento.valor_seguro
		lucro = lucro - investimento.outros_gastos
	for corrida in corridas:
		lucro = lucro + corrida.valor
	return render(request, 'lucro.html', {'info_lucro': lucro}, {'lista_investimentos', investimentos})
	
class CriarInvestimento(CreateView):
    model = Investimento
    fields = '__all__'
    template_name = 'criar-investimento.html'
    success_url = '.'