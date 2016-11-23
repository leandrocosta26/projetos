class smtp_client(object):
	"""docstring for smtp_client"""
	def __init__(self, user, password, smtp, to):
		self.user = user
		self.password = password
		self.smtp = smtp
		self.to = to
		