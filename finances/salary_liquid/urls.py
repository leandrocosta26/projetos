from django.conf.urls import url, include
from . import views 

urlpatterns = [
    url(r'^index/(?P<sal>\d+$)', views.index),
]
