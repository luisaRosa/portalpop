# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# modelo de agendamento
class Agendamento(models.Model):

    class Meta:
        db_table = 'agendamento' # nome da tabela no banco de dados

   
    assunto = models.CharField('Assunto', max_length=45)
    data = models.DateTimeField('dt.Agendamento')
    horaEntrada = models.TimeField('hora.Entrada')
    horaSaida = models.TimeField(u'hora_Saida')
    instituicao = models.CharField(u'Instituicao',max_length=45)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)


    def __unicode__(self):
        return self.assunto

		
# modelo da categoria das noticias
class CategoriaNoticia(models.Model):

	class Meta:
	    db_table = 'categoriaNoticia' # nome da tabela no banco de dados
	
	categoria = models.CharField('Categoria', max_length=45, help_text='Obrigatório. 45 caracteres ou menos.')
	
	def __unicode__(self):
		return self.categoria
	
	
# modelo da categoria dos Boletins de ocorrência
class CategoriaBo(models.Model):
	class Meta:
		db_table = 'categoriaBos' # nome da tabela no banco de dados
		
	categoria = models.CharField('Categoria', max_length=45, help_text='45 caracteres ou menos.')
	
	def __unicode__(self):
		return self.categoria
	

# modelo da noticia
class Noticia(models.Model):
	
	class Meta:
		db_table= 'noticia'
	
	title = models.CharField('Título', max_length=100, help_text='100 caracteres ou menos.')
	descricao= models.TextField('Descrição', max_length=500, help_text='500 caracteres ou menos.')
	imagem = models.ImageField('Imagem')
	data= models.DateTimeField('Publicação')
	texto = models.TextField('Texto', max_length=2048, help_text='2048 caracteres ou menos.')
	status= models.BooleanField('Publicada', default='False')
	categoria=models.ForeignKey( CategoriaNoticia)
	administrador = models.ForeignKey(settings.AUTH_USER_MODEL, default=settings.AUTH_USER_MODEL)
	
	def __unicode__(self):
		return self.title
		

# modelos dos boletins de ocorrência
class Bo (models.Model):

	IMPACTO_CHOICES = (('x', 'Muito baixo'),('xx', 'Baixo'), ('xxx', 'Médio'), 
		('xxxx', 'Alto'), ('xxxxx', 'Muito alto'))
	class Meta:
		db_table = 'Boletins'
		
	titulo= models.CharField('Título', max_length=100, help_text=' 100 caracteres ou menos.')
	impacto= models.CharField('Impacto', max_length=5, choices=IMPACTO_CHOICES, default='x')
	texto = models.TextField('Texto', max_length=500, help_text='500 caracteres ou menos.')
	categoria = models.ForeignKey(CategoriaBo)
	data = models.DateTimeField('')
	administrador = models.ForeignKey(settings.AUTH_USER_MODEL, default=settings.AUTH_USER_MODEL)
	
	def __unicode__(self):
		return self.titulo
	

   


# modelo dos pops
class Pop(models.Model):
    class Meta:
        db_table = 'pops' # nome da tabela no banco de dados


    sigla = models.CharField('Sigla', primary_key='true', max_length=6, help_text='Obrigatório. 6 caracteres ou menos.')
    site = models.CharField('Site',max_length=45, help_text='45 caracteres ou menos.')
    contato = models.CharField('Contato',max_length=45, help_text='45 caracteres ou menos.')

    def __unicode__(self):
        return self.sigla


