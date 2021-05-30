from __future__ import unicode_literals

from django.db import models
from taxistas.models import Taxista

# Create your models here.
class Investimento(models.Model):
	combustivel = models.FloatField()
	valor_combustivel = models.FloatField()
	valor_IPVA = models.FloatField()
	valor_seguro = models.FloatField()
	outros_gastos = models.FloatField()
	taxista = models.ForeignKey(Taxista, blank=True, null=True)
	data_investimento = models.DateField(null=True)
	
	def __str__(self):
		return str(self.data_investimento)