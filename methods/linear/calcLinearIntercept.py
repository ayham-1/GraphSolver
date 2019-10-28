class LinearIntercept:
	"""Class to calculate linear intercept"""

	def calc_intercept(self, x, y):

		self.x = x
		self.y = y
		y1 = (self.x + self.y) / 3
		y2 = ((3 * self.x) - (2 * y1)) / 4
		return y2
