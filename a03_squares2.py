triangles = list()

f = open('a03_input.txt', 'r')
for line in f:
    line = line.strip('\n')
    if line:
        triangle = [int(x) for x in line.split()]
        triangles.append(triangle)

# Strategy:
# * Step through the initial list of triangles by 3 so we can grab 3 at a time.
# * Use zip() function to take first three elements of three lists together
#   into their own list, then the second elements, then the third elements.

alternate_triangles = list()
for i in range(0,len(triangles), 3):
    for t in zip(triangles[i], triangles[i+1], triangles[i+2]):
        alternate_triangles.append(t)

possible_triangles = 0

for t in alternate_triangles:
    if (t[0] < t[1] + t[2] and
        t[1] < t[0] + t[2] and
        t[2] < t[1] + t[0]):
        possible_triangles += 1

print(f'Possible triangles = {possible_triangles}')
      
