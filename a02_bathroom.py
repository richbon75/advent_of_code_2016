
instructions = list()

f = open('a02_input.txt', 'r')
for line in f:
    line = line.strip('\n')
    if line:
        instructions.append(line)
f.close()

keypad = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']]

directions = {
    'U': [-1,  0],
    'D': [ 1,  0],
    'L': [ 0, -1],
    'R': [ 0,  1]
    }

current_location = [1,1]  # start at '5'

code = ''

def move(direction, current_location):
    # apply movement
    current_location = [sum(x) for x in zip(current_location, directions[direction])]
    # don't fall off edges of keypad
    if current_location[0] < 0:
        current_location[0] = 0
    elif current_location[0] > 2:
        current_location[0] = 2
    if current_location[1] < 0:
        current_location[1] = 0
    elif current_location[1] > 2:
        current_location[1] = 2
    return current_location

for instruction in instructions:
    for letter in instruction:
        current_location = move(letter, current_location)
        # print(letter, current_location)
    code += keypad[current_location[0]][current_location[1]]

print('Bathroom code: {}'.format(code))

    

