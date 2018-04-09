
instructions = list()

f = open('a02_input.txt', 'r')
for line in f:
    line = line.strip('\n')
    if line:
        instructions.append(line)
f.close()

# Approach:
# * Same basic logic as first version, but to cut down on
#   weird keypad bounding logic, I made the keypad matrix bigger
#   and now check to make sure we're not moving into a "None"
#   value. If we would, don't make the move.

N = None

keypad = [
    [N, N , N , N , N , N , N ],
    [N, N , N ,'1', N , N , N ],
    [N, N ,'2','3','4', N , N ],
    [N,'5','6','7','8','9', N ],
    [N, N ,'A','B','C', N , N ],
    [N, N , N ,'D', N , N , N ],
    [N, N , N , N , N , N , N ]]

directions = {
    'U': [-1,  0],
    'D': [ 1,  0],
    'L': [ 0, -1],
    'R': [ 0,  1]
    }

current_location = [3,1]  # start at '5'

code = ''

def move(direction, current_location):
    # apply movement
    check = [sum(x) for x in zip(current_location, directions[direction])]
    # don't fall off edges of keypad
    if keypad[check[0]][check[1]] is not None:
        current_location = check
    return current_location

for instruction in instructions:
    for letter in instruction:
        current_location = move(letter, current_location)
    code += keypad[current_location[0]][current_location[1]]

print('Bathroom code: {}'.format(code))

    

