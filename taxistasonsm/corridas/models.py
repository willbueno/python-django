from __future__ import unicode_literals

from django.db import models
from taxistas.models import Taxista

# Create your models here.
class Corrida(models.Model):
	data_corrida = models.DateField()
	endereco_origem = models.CharField(max_length=200)
	endereco_destino = models.CharField(max_length=200)
	horario_partida = models.TimeField(blank=True, null=True)
	horario_chegada = models.TimeField(blank=True, null=True)
	distancia = models.FloatField()
	valor = models.FloatField()
	dinheiro = models.BooleanField(default=False)
	cartao = models.BooleanField(default=False)  # default eh com dinheiro (false)
	taxista = models.ForeignKey(Taxista, blank=True, null=True)
	
	def __str__(self):
		return str(self.data_corrida)