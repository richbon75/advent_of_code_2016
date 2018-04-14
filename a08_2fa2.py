
from collections import namedtuple

Instruction = namedtuple('Instruction','instruction,arg1,arg2')

instructions = list()

f = open('a08_input.txt','r')
for line in f:
    line = line.strip()
    parts = line.split()
    if parts[0] == 'rect':
        instructions.append(Instruction(parts[0],
                                        int(parts[1].split('x')[0]),
                                        int(parts[1].split('x')[1])))
    else:
        instructions.append(Instruction(parts[1],
                                        int(parts[2].split('=')[1]),
                                        int(parts[4])))
f.close()


class Screen(object):

    def __init__(self, rows=6, cols=50):
        '''Initialize the screen.'''
        self.screen = [['.']*cols for _ in range(rows)]

    def display(self):
        '''Print out the screen.'''
        for row in self.screen:
            print(''.join(row))

    def draw_rect(self, c, r):
        '''Draw a rectangle in the upper left of size c, r'''
        for i in range(r):
            for j in range(c):
                self.screen[i][j] = '#'

    def rotate_row(self, r, places):
        '''Rotates the row right a given number of places.'''
        if not places:
            return
        places = places % len(self.screen[r])
        self.screen[r] = self.screen[r][-places:] + self.screen[r][:-places]

    def rotate_col(self, c, places):
        '''Rotates the column down a given number of places.'''
        if not places:
            return
        height = len(self.screen)
        places = places % height
        for _ in range(places):
            temp = self.screen[0][c]
            for i in range(height):
                self.screen[(i+1)%height][c], temp = temp, self.screen[(i+1)%height][c]

    def lit_pix(self):
        '''Count the number of lit pixels'''
        lit = 0
        for i in range(len(s.screen)):
            for j in range(len(s.screen[0])):
                if s.screen[i][j] == '#':
                    lit += 1
        return lit

s = Screen()
for i in instructions:
    if i.instruction == 'rect':
        s.draw_rect(i.arg1, i.arg2)
    elif i.instruction == 'row':
        s.rotate_row(i.arg1, i.arg2)
    else:
        s.rotate_col(i.arg1, i.arg2)
print(f'Pixels lit = {s.lit_pix()}')
s.display()



        
