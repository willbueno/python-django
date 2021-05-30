from django.conf.urls import url
from . import views
from corridas.views import CriarCorrida

urlpatterns = [
	url(r'^$',views.corridas, name='corridas'),
	url(r'^(?P<id>[0-9]+)/$', views.corrida, name='corrida'),
	url(r'^criar/$', CriarCorrida.as_view(), name='criar_corrida'), 
]
