
f = open('a01_input.txt')
for line in f:
    line = line.strip()
    if line:
        directions = line.split(',')
f.close()

directions = [d.strip() for d in directions]

# Approach:
#  * Location stores our North/South distance and East/West distance from origin.
#  * Track our orientation by a list of headings, which we can rotate
#    through clockwise by +1 to the index (Right turns),
#    and counterclockwise by -1 (Left turns).
#  * We add or subtract distances travelled by our heading, and the
#    headings list gives us that multiplier to determine + or -.

location = [0, 0]  # first is North/South, second is East/West
headings = [('N', 1),
            ('E', 1),
            ('S', -1),
            ('W', -1)]
current_heading = 0

for d in directions:
    if d[0] == 'R':
        current_heading = (current_heading + 1) % 4
    else:
        current_heading = (current_heading - 1) % 4
    go_blocks = int(d[1:])
    location[current_heading % 2] += headings[current_heading][1] * go_blocks

print('Headquarters is {} blocks away.'
      .format(abs(location[0]) + abs(location[1])))
