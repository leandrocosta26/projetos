from django.db import models

class Missing(models.Model):
	name = models.CharField(max_length=255, null=False)
	age = models.BigIntegerField(null=False)
	hair_color = models.CharField(max_length=255, null=False)
	eye_color = models.CharField(max_length=255, null=False)
	height = models.FloatField(null=False)
	skin_color = models.CharField(max_length=255, null=False)
	approximate_weight = models.FloatField(null=False)
	user_id = models.BigIntegerField(null=False)
	street = models.CharField(max_length=255, null=False)
	city = models.CharField(max_length=255, null=False)
	state = models.CharField(max_length=255, null=False)
	country = models.CharField(max_length=255, null=False)
	district = models.CharField(max_length=255, null=False)
	approximate_number = models.BigIntegerField(null=True)
