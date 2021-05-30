from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Taxista(models.Model):
	nome = models.CharField(max_length = 200)
	endereco = models.CharField(max_length = 200)
	data_nascimento = models.DateField()
	DDD = models.IntegerField(default = 51)
	telefone = models.IntegerField()
	rg = models.IntegerField()
	cpf = models.IntegerField()
	placa_carro = models.CharField(max_length = 200)
	marca_carro = models.CharField(max_length = 50)
	Serial_number_do_aparelho_integrato = models.IntegerField()
	##email = models.
	##password = model.
	
	def __str__(self):
		return str(self.nome)