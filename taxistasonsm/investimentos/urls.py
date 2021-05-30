from django.conf.urls import url
from . import views
from investimentos.views import CriarInvestimento
from investimentos.views import lucro

urlpatterns = [
	url(r'^$',views.investimentos, name='investimentos'),
	url(r'^(?P<id>[0-9]+)/$', views.investimento, name='investimento'),
	url(r'^criar/$', CriarInvestimento.as_view(), name='criar_investimento'), 
]