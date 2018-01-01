
class Judge:

	def __init__(self, A, B):
		self.A = A
		self.B = B
		self.total = 0

	def __next__(self):
		next(self.A)
		next(self.B)
		self.total += (self.A.first16() == self.B.first16())

	def find_matches(self, rounds_to_consider):
		for i in list(range(rounds_to_consider)):
			if i % 1000000 == 0:
				print("Considered " + str(i) + " matches so far", end = "\r")
			next(self)

class Generator:

	def __init__(self, value, factor):
		self.value = value
		self.factor = factor

	def __next__(self):
		self.value = (self.value * self.factor) % 2147483647
		return self

	def __repr__(self):
		return str(self.value)

	def first16(self):
		return ''.join(list(reversed(bin(self.value)[2:])))[:16]

if __name__ == '__main__':
	# Test input
	A = Generator(65, 16807)
	B = Generator(8921, 48271)
	judge = Judge(A, B)
	# The line below take several minutes to run when uncommented
	# judge.find_matches(40000000)
	print(judge.total)

	# Real input
	A = Generator(783, 16807)
	B = Generator(325, 48271)
	judge = Judge(A, B)
	# The line below take several minutes to run
	judge.find_matches(40000000)
	print(judge.total)




