from django.shortcuts import render, get_object_or_404, redirect
from .models import Taxista
from django.views.generic import CreateView
# Create your views here.
def taxistas(request):
	taxistas = Taxista.objects.all()
	return render(request, 'taxistas.html', {'lista_taxistas': taxistas})

def taxista(request, taxista_id):
	taxista = get_object_or_404(Taxista,pk=taxista_id)
	return render(request, 'taxista.html', {'taxista': taxista})

def login(request):
    if request.method == 'POST':
        login = request.POST['login']
        senha = request.POST['senha']
        return redirect('index')

    else:
            return render(request, 'login.html')
	
class CriarTaxista(CreateView):
    model = Taxista
    fields = '__all__'
    template_name = 'criar-taxista.html'
    success_url = '.'