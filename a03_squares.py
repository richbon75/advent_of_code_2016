triangles = list()

f = open('a03_input.txt', 'r')
for line in f:
    line = line.strip('\n')
    if line:
        triangle = [int(x) for x in line.split()]
        triangles.append(triangle)

possible_triangles = 0

for t in triangles:
    if (t[0] < t[1] + t[2] and
        t[1] < t[0] + t[2] and
        t[2] < t[1] + t[0]):
        possible_triangles += 1

print(f'Possible triangles = {possible_triangles}')
      
