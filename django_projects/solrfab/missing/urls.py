from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^missing/(?P<id_missing>\d+)/information$', views.information, name='view_information'),
    url(r'^missing/registrar/$', views.MissingRegistrationView.as_view(), name='registrar_missing')
]
