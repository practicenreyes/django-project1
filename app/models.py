from django.db import models

# Create your models here.
class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)

	def __str__(self):
		return self.titulo

class Enlace(models.Model):
	categoria = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length = 140)
	enlace = models.URLField()
	votos = models.IntegerField(default = 0)
	
	def __str__(self):
		return "{0} - {1}" .format(self.titulo, self.enlace)