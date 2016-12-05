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

    def valid_triangle_count(self):
        return sum([t.valid() for t in self.triangles])

class Triangle:

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

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
    print(triangles.valid_triangle_count())
    # Correct answer is 917
    


