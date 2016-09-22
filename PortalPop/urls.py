"""PortalPop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import logout_then_login
from django.core.urlresolvers import reverse_lazy
from PortalPopAc.views import index, acessar, agendamento_videoconferencia, cadastra_usuario, contato, \
    editar_usuarios, servicos, clientes, outrospops




sair = lambda request, **kwargs : logout_then_login(request, login_url=reverse_lazy('home'), **kwargs)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name='index'),
    url(r'^$', index, name="home"),  # AQUI
    url(r'^cadastra_usuario/$', cadastra_usuario, name='cadastra_usuario'),
    url(r'^agendamento_videoconferencia/$', agendamento_videoconferencia, name='agendamento_videoconferencia'),
    url(r'^acessar/$', acessar, name="acessar"),
    url(r'^contato/$', contato, name='contato'),
    url(r'^editar_usuarios/$', editar_usuarios, name='editar_usuarios'),
    url(r'^logout/$', sair, name="logout"),
    url(r'^servicos/', servicos, name='servicos'),
    url(r'^clientes/', clientes, name='clientes'),
    url(r'^outrospops/', outrospops, name='outrospops'),
    url(r'^static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}), # AQUI
    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
