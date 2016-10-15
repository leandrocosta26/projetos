from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100, null=False)
	email = models.CharField(max_length=255, null=False)
	phone = models.CharField(max_length=15, null=False)
	password = models.CharField(max_length=100, null=False)
	