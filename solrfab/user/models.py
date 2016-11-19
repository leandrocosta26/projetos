from django.contrib.auth.models import User
from django.db import models

class Profiler(models.Model):

	def content_file_name(instance, filename):
		return ("./image/%s/%s" % (instance.user.username, filename))


	username = models.CharField(max_length=255, null=False)
	image = models.ImageField(upload_to = content_file_name, default = 'images/no-img.jpg')
	user = models.OneToOneField(User, related_name='user_profile')
