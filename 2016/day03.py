# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth of 
# hallways and office furniture that makes up this part of Easter Bunny HQ. 
# This must be a graphic design department; the walls are covered in 
# specifications for triangles.

# Or are they?
#
# The design document gives the side lengths of each triangle it describes,
# but... 5 10 25? Some of these aren't triangles. You can't help but mark 
# the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the 
# remaining side. For example, the "triangle" given above is impossible, 
# because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?
#
# --- Part Two ---
#
# Now that you've helpfully marked up their design documents, it occurs to you 
# that triangles are specified in groups of three vertically. 
# Each set of three numbers in a column specifies a triangle. 
# Rows are unrelated.
#
# For example, given the following specification, numbers with the same 
# hundreds digit would be part of the same triangle:
#
#  101 301 501
#  102 302 502
#  103 303 503
#  201 401 601
#  202 402 602
#  203 403 603
#
#  In your puzzle input, and instead reading by columns, 
#  how many of the listed triangles are possible?
#
# ----------------------------------------------------------------------------

import re

class TriangleList:

    def __init__(self, triangle_text):
        self.triangle_list = re.split('\n', triangle_text)
        self.triangles = []

    def parse_list(self):
        for line in self.triangle_list:
            self.parse_line(line)

    def parse_line(self, text_line):
        dims = re.findall('[0-9]+', text_line)
        dims = [int(x) for x in dims]
        self.triangles.append(Triangle(dims[0], dims[1], dims[2]))
        return dims

    def parse_list2(self):
        sets = int(len(self.triangle_list) / 3)
        for i in range(sets):
            self.parse_set2(self.triangle_list[(i*3):(i*3+3)])
        
    def parse_set2(self, set):
        lines = [re.findall('[0-9]+', line) for line in set]
        self.triangles.append(Triangle(lines[0][0], lines[1][0], lines[2][0]))
        self.triangles.append(Triangle(lines[0][1], lines[1][1], lines[2][1]))
        self.triangles.append(Triangle(lines[0][2], lines[1][2], lines[2][2]))

    def valid_triangle_count(self):
        return sum([t.valid() for t in self.triangles])

class Triangle:

    def __init__(self, s1, s2, s3):
        self.s1 = int(s1)
        self.s2 = int(s2)
        self.s3 = int(s3)

    def sides(self):
        return (self.s1, self.s2, self.s3)

    def valid(self):
        sides = [self.s1, self.s2, self.s3]
        m = max(sides)
        m_index = [i for i in range(0, 3) if sides[i]==m][0]
        smaller_indicies = [i for i in range(0, 3) if i != m_index]
        smaller_sides = [sides[i] for i in smaller_indicies]
        return sum(smaller_sides) > m

if __name__ == '__main__':
    fileobject = open('inputs/day03.txt')
    data = fileobject.read()
    triangles = TriangleList(data)
    triangles.parse_list()
    print("Part 1: ", triangles.valid_triangle_count())
    # Correct answer is 917
    triangles = TriangleList(data)
    triangles.parse_list2()
    print("Part 2: ", triangles.valid_triangle_count())
    # Correct answer is 1649
    


