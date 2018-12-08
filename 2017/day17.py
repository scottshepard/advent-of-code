import time

class Spinlock:

	def __init__(self, step):
		self.step = step
		self.values = [0]
		self.index = 0
		self.next_val = 1
		self.time = time.time()

	def __next__(self):
		if self.next_val % 100000 == 0:
			print('That 100,000 cycles took ' + str(time.time() - self.time) + ' seconds', end='\n')
			self.time = time.time()
		self.index = (self.index + self.step) % len(self.values) + 1
		self.values.insert(self.index, self.next_val)
		self.next_val += 1
		return self

	def __repr__(self):
		return str(self.values)

	def cycle(self, n):
		for i in range(n):
			next(self)
		return self

if __name__ == '__main__':
	s0 = Spinlock(3)
	s0.cycle(2017)
	print(s0.values[s0.index+1])

	s1 = Spinlock(335)
	s1.cycle(2017)
	print(s1.values[s1.index+1])	

	s2 = Spinlock(335)

	t0 = time.time()
	s2.cycle(1000000)
	t1 = time.time()

	print(t1 - t0)
