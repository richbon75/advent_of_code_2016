from collections import Counter

f = open('a01_input.txt')
for line in f:
    line.strip()
    if line:
        directions = line.split(',')
f.close()

directions = [d.strip() for d in directions]

location = [0, 0]  # first is North/South, second is East/West
headings = [('N', 1),
            ('E', 1),
            ('S', -1),
            ('W', -1)]
current_heading = 0

locations_visited = Counter()
locations_visited[(0,0)] = 1
spot_found = False

for d in directions:
    if d[0] == 'R':
        current_heading = (current_heading + 1) % 4
    else:
        current_heading = (current_heading - 1) % 4
    go_blocks = int(d[1:])
    # "Visit" means walk past, so we have to take the time to visit each block,
    # we can't just "jump" the number of blocks in the direction.
    for _ in range(0, go_blocks):
        location[current_heading % 2] += headings[current_heading][1]
        locations_visited[tuple(location)] += 1
        if locations_visited[tuple(location)] == 2:
            print('The first location we visited twice is {} blocks away.'
                  .format(abs(location[0])+abs(location[1])))
            spot_found = True
            break
    if spot_found:
        break

