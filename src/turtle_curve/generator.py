from abc import ABC, abstractmethod


class NumberGenerator(ABC):
	'''Base class for a number generator'''

	@abstractmethod
	def __iter__(self):
		'''Method for creating an iter object'''


	@abstractmethod
	def __next__(self):
		'''Method for getting the next number'''


class FractionGenerator(NumberGenerator):
	'''Generate every digit in the fraction 1/n'''

	def __init__(self, n: int, max_iter=10_000):
		self.n = n
		self.max_iter = max_iter

	def __iter__(self):
		self.remainder = 1
		self.i = 0
		return self

	def __next__(self):
		if self.remainder == 0 or self.i == self.max_iter:
			raise StopIteration

		self.i += 1

		quotient, self.remainder = divmod(self.remainder, self.n)

		self.remainder *= 10

		return quotient