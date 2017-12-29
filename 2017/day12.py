import os
import re

class Village:

	def __init__(self, lines):
		self.programs = {}
		self.parse_lines(lines)
		self.groups = []
		self.all_group_items = []

	def parse_lines(self, lines):
		for line in lines:
			self.parse_line(line)

	def parse_line(self, line):
		line = re.sub(',', '', line)
		chars = line.split(' ')
		chars.pop(1)
		ids = [int(i) for i in chars if i != ',']
		root = ids.pop(0)
		self.add_program(root)
		root = self.programs[root]
		for id in ids:
			self.add_program(id)
			self.programs[id].add_linked_program(root)

	def add_program(self, id):
		if id not in self.programs.keys():
			self.programs[id] = Program(id)

	def collect_all_groups(self):
		for program in list(self.programs.values()):
			self.collect(program)
		return self.groups

	def collect(self, program):
		if program.id not in self.all_group_items:
			group = program.collect()
			self.groups.append(group)
			self.all_group_items += group


class Program:

	def __init__(self, id):
		self.id = id
		self.linked = {}

	def __repr__(self):
		return str(self)

	def __str__(self):
		return 'P' + str(self.id)

	def add_linked_program(self, program):
		if program.id not in self.linked.keys():
			self.linked[program.id] = program
			program.add_linked_program(self)

	def collect(self, group=[]):
		if self.id not in group:
			group.append(self.id)
		for linked in list(self.linked.values()):
			if linked.id not in group:
				linked.collect(group)
		return group




if __name__ == '__main__':
    rel_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(rel_path, "inputs/day12.txt")
    f = open(file_path)
    data = f.read().split('\n')
    v = Village(data)
    print(len(v.programs[0].collect()))
    print(len(v.collect_all_groups()))
