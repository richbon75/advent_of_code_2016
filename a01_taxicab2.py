
f = open('a01_input.txt')
for line in f:
    line = line.strip()
    if line:
        directions = line.split(',')
f.close()

directions = [d.strip() for d in directions]

# Approach:
# * Same location/heading tracking features as the first version.
# * Can't "jump" across distances by adding them, because we need
#   to "visit" each location we would travel through. So now we just
#   iterate through each distance by 1's or -1's.
# * Track locations visited with a set. Since we stop after we've
#   already been somewhere once, we don't need the full count.

location = [0, 0]  # first is North/South, second is East/West
headings = [('N', 1),
            ('E', 1),
            ('S', -1),
            ('W', -1)]
current_heading = 0

locations_visited = set()
locations_visited.add(tuple(location))  # add the origin, since we're here.
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
        if tuple(location) in locations_visited:
            print('The first location we visited twice is {} blocks away.'
                  .format(abs(location[0])+abs(location[1])))
            spot_found = True
            break
        locations_visited.add(tuple(location))
    if spot_found:
        break

