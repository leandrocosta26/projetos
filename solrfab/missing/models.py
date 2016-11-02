from django.db import models
from user.models import UserProfiler

class Missing(models.Model):

	def content_file_name(instance, filename):
		return ("./image/%s/%s" % (instance.user.username, filename))

	name = models.CharField(max_length=255, null=False)
	age = models.BigIntegerField(null=False)
	hair_color = models.CharField(max_length=255, null=False)
	eye_color = models.CharField(max_length=255, null=False)
	height = models.FloatField(null=False)
	skin_color = models.CharField(max_length=255, null=False)
	approximate_weight = models.FloatField(null=False)
	user = models.ForeignKey(UserProfiler, related_name='user_owner')
	street = models.CharField(max_length=255, null=False)
	city = models.CharField(max_length=255, null=False)
	state = models.CharField(max_length=255, null=False)
	country = models.CharField(max_length=255, null=False)
	district = models.CharField(max_length=255, null=False)
	approximate_number = models.BigIntegerField(null=True)
	gender = models.CharField(max_length=1, null=True)
	image = models.ImageField(upload_to = content_file_name)
	cloutes = models.CharField(max_length=255, null=True)
	reason = models.CharField(max_length=255, null=True)

	