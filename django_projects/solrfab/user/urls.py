from django.conf.urls import url
from django.contrib import admin
from user.views import UserView

urlpatterns = [
    url(r'^create', UserView.as_view(), name='create_user'),
]
