class MissingException(Exception):

	def __init__(self, message):
		super(MissingException, self).__init__()
		self.message = message

	def __str__(self):
		return repr(self.message)
