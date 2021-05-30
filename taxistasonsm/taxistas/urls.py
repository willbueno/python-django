from django.conf.urls import url
from . import views
from taxistas.views import CriarTaxista

urlpatterns = [
	url(r'^$',views.taxistas, name='taxistas'),
	url(r'^(?P<taxista_id>[0-9]+)/$', views.taxista, name='taxista'),
	url(r'^criar/$', CriarTaxista.as_view(), name='criar_taxista'), 
]