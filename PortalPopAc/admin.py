# coding=utf-8
from django.contrib import admin
from .models import CategoriaNoticia
from .models import CategoriaBo
from .models import Noticia
from .models import Bo
from .models import Pop
from .models import Agendamento
from django.core.mail import send_mail
from django.contrib import messages

# registro dos modelos para aparecer na interface do administrador
class AgendamentoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Agendamento de Videoconferência", {'fields': ['assunto', 'instituicao', 'data', 'horaEntrada', 'horaSaida','usuario',
                                                        'confirmaAgendamento',
    ]})]
    
class NoticiaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Adicionar notícias", {'fields': ['title','categoria', 'descricao', 'texto', 'imagem','data','administrador'
                            ]})]

class BoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Adicionar Boletim de Ocorrência", {'fields': ['titulo','categoria','impacto', 'texto','data','administrador'
                            ]})]
							
class PopAdmin(admin.ModelAdmin):
	fieldsets = [
		("Adicionar Pops do Brasil", {'fields': ['sigla', 'site', 'contato']})
	]
	
class categoriaNoticiaAdmin(admin.ModelAdmin):
	fieldsets = [
		("Adicionar Categoria das Notícias", {'fields':[ 'categoria']})
	]
	
class categoriaBosAdmin(admin.ModelAdmin):
	fieldsets = [
		("Adicionar Categoria dos Boletins de Ocorrência", {'fields':[ 'categoria']})
	]

admin.site.register(CategoriaBo, categoriaBosAdmin)
admin.site.register(CategoriaNoticia, categoriaNoticiaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Bo, BoAdmin)
admin.site.register(Pop, PopAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)

