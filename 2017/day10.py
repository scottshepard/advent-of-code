import os

class KnotHash:

	def __init__(self, input, nums = list(range(256)), dh = True):
		self.nums = nums
		self.input = input
		self.pos = 0
		self.skip_size = 0
		self.sparse_hash = self.sparse_hash()
		if dh:
			self.hash = self.dense_hash(self.sparse_hash)

	def __repr__(self):
		return self.hash

	def dense_hash(self, sh):
		dh = [None] * 16
		for i in list(range(16)):
			section = [sh[j] for j in list(range(i*16, (i+1)*16))]
			result = section[0]
			for j in list(range(1, 16)):
				result = result ^ section[j]
			dh[i] = str(format(result, '02x'))
		return ''.join(dh)

	def sparse_hash(self):
		for i in list(range(64)):
			ascii_ints = self.string_ascii_converter(list(self.input)) + [17, 31, 73, 47, 23]
			self.nums = self.knot_hash_round(self.nums, ascii_ints, self.pos, self.skip_size)
		return self.nums

	def knot_hash_simple(self):
		rev_len_list = [int(d) for d in self.input.split(',')]
		return self.knot_hash_round(self.nums, rev_len_list)

	def knot_hash_round(self, nums, rev_len_list, pos=0, skip_size=0):
		if len(rev_len_list) == 0:
			return nums
		rev_len = rev_len_list.pop(0)
		hashed_nums = self.knot_hash_step(nums, rev_len, pos)
		pos = (pos + rev_len + skip_size) % len(nums)
		skip_size += 1
		self.pos = pos
		self.skip_size = skip_size
		return self.knot_hash_round(hashed_nums, rev_len_list, pos, skip_size)

	def knot_hash_step(self, nums, rev_len, pos):
		i_in_rev = [i % len(nums) for i in list(range(pos, pos + rev_len))]
		rev_lst = self.rev([nums[i] for i in i_in_rev])
		i_not_in_rev = list(set(list(range(len(nums)))) - set(i_in_rev))
		lst = [None] * (len(nums))
		for i in list(range(len(i_in_rev))):
			rev_i = i_in_rev[i]
			lst[rev_i] = rev_lst[i]
		for i in i_not_in_rev:
			lst[i] = nums[i]
		return lst

	def rev(self, l):
		return list(reversed(l))

	def string_ascii_converter(self, string):
		return [ord(c) for c in list(string)]

if __name__ == '__main__':    
    test_data = '3,4,1,5'
    test_nums = [0, 1, 2, 3, 4]
    kh = KnotHash(test_data, test_nums, False)
    print(kh.sparse_hash)

    input = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
    kh = KnotHash(input)
    hashed = kh.sparse_hash
    print(hashed[0] * hashed[1])

    print(KnotHash(input))


