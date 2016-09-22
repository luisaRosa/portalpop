# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import UpdateView

from .models import Noticia
from .models import Bo
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from .form import UsuarioForm, ContactForm, AgendamentoForm, EditarUsuarioForm



# Create your views here.
class UpdateProfile(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'username',] # Keep listing whatever fields
    # the combined UserProfile and User exposes.
    template_name = 'edicaoUsuarios.html'


@transaction.atomic
def cadastra_usuario(request):
 
  if request.method == 'POST':
    form = UsuarioForm(request.POST)

    if form.is_valid():
      # grava o usuário
      usuario = form.save()
      
      # atribui a senha criptografada e ativa o usuário
      usuario.set_password( usuario.password )
      usuario.is_active = True
      usuario.save()
      
      # efetua o login
      auth_login(request, usuario)

      # envia o email de confirmação
      form.enviar()

      # adiciona mensagem de que o cadastro está OK
      messages.add_message(request, messages.INFO, 'Seu cadastro foi efetuado com sucesso!')
      
      # tudo deu certo, então, vai para o index
      return redirect(reverse_lazy('index'))
      
      
  else:
      form = UsuarioForm()
      
  return render(request, 'cadastroUsuario.html',{'form': form})



def index(request):

    form1 = ContactForm() #carrega o formulário de contato
    form = UsuarioForm() #carrega o formulário de cadastro de usuário
    form2 = EditarUsuarioForm(request)
    noticias = Noticia.objects.filter(status='False').order_by('-id')[:4] # pega as 4 notícias mais novas para colocar na página
    bos = Bo.objects.order_by('-data')[:5] # pega os 5 boletins de ocorrência mais novos para colocar na página
    try:
        usuario = User.objects.get(pk=request.user.id)
    except ObjectDoesNotExist:
        pass

    return render(request, 'index.html', locals())

def servicos(request):

    form1 = ContactForm()#carrega o formulário de contato
    form = UsuarioForm()#carrega o formulário de cadastro de usuário

    return render(request, 'servicos.html', locals())

def clientes(request):

    form1 = ContactForm()  # carrega o formulário de contato
    form = UsuarioForm()  # carrega o formulário de cadastro de usuário

    return render(request, 'clientes.html', locals())

def outrospops(request):

    form1 = ContactForm()  # carrega o formulário de contato
    form = UsuarioForm()  # carrega o formulário de cadastro de usuário

    return render(request, 'outrospops.html', locals())

def acessar(request):

    if request.method == 'POST':
        usuario = request.POST.get('username', '')
        senha = request.POST.get('password', '')
        usuario = authenticate(username=usuario, password=senha)
        if usuario:
            messages.add_message(request, messages.WARNING, u'Seja bem vindo %s' % usuario)
            auth_login(request, usuario)

            if usuario.is_superuser:
                return redirect(reverse_lazy('admin:index'))

        else:
            messages.add_message(request, messages.WARNING, u'Usuário ou Senha incorreta')

        if request.GET.get('next', None):
            return redirect(request.GET.get('next', None))
    return redirect(reverse_lazy('index'))

@login_required()
def agendamento_videoconferencia(request):

        form2 = AgendamentoForm()
        form1 = ContactForm()
        form = UsuarioForm()


        if request.method == 'POST':
            form2 = AgendamentoForm(request.POST)

            if form2.is_valid():
                # grava agendamento
                agendamento = form2.save(commit=False)

                data = request.POST.get('data','')
                horaEntrada = request.POST.get('horaEntrada','')
                horaSaida = request.POST.get('horaSaida','')
                agendamento.data = data
                agendamento.horaEntrada = horaEntrada
                agendamento.horaSaida = horaSaida
                user = User.objects.get(pk=request.user.id)  # pega o usuário que está logado
                email = user.email
                first_name = user.first_name
                agendamento.usuario = user # seta o usuário que fez o agendamento
                agendamento.save()

                titulo = "Confirmação do agendamento da sala de videoconferencia"
                destino = ''+email
                texto = u"""
                      Olá, """+first_name+u"""!

                      Seu agendamento da sala de videoconferência no portal do PoP-AC foi aceito.

                      Dados do agendamento:
                          Data: """+data+u"""
                          Horário de Entrada: """+horaEntrada+u"""
                          Horário de Saída: """+horaSaida+u"""

                      Esse é um email automático, não precisa responder! Caso voce não tenha realizado nenhum cadastro ignore essa mensagem.
                                 """
                try:
                    send_mail(
                        subject=titulo,
                        message=texto,
                        from_email=destino,
                        recipient_list=[destino]
                    )
                    messages.add_message(request, messages.INFO,
                                         u'Seu Agendamento foi solicitado, aguarde confirmação dos administradores!')
                    form2 = AgendamentoForm()
                except BadHeaderError, SMTPException:
                    messages.add_message(request, messages.ERROR,
                                         'Ocorreu um problema ao enviar a sua mensagem. Porfavor tente novamente!')







            else:
                form2 = AgendamentoForm()
        return  render(request, 'agendamento_videoconferencia.html', locals())


def contato(request):

    form = ContactForm();
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                form.enviar()
                messages.add_message(request, messages.INFO,
                                 'Sua mensagem foi enviada com sucesso!')
                return redirect(reverse_lazy('index'))
            except BadHeaderError:
                messages.add_message(request, messages.ERROR,
                                     'Ocorreu um problema ao enviar a sua mensagem. Porfavor tente novamente!')


    else:
        form = ContactForm()


    return render(request, 'contato.html', {
        'form': form,
    })

def editar_usuarios(request):
    pass