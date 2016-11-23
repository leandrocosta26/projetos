from django.conf.urls import url
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views

urlpatterns = [
    url(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar'),
    url(r'^login/$', views.login, {'template_name' : 'login.html'} , name='login'),
    url(r'^logout/$',views.logout_then_login, {'login_url' : '/login/'} ,name='logout')
]