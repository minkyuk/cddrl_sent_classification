class params(object):
	def __init__(self):
		self.rmpc = 1
		self.weightparam = 1e-3

	def __str(self):
		t = "rmpc", self.rmpc, "weightparam", self.a
		t = map(str, t)
		return ' '.join(t)
