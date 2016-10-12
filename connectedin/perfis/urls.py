from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir),
    url(r'^perfis/email/(?P<email>\w+)$', views.search_by_email)
]
