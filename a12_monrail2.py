class bunnymachine(object):
    '''Define a virtual computer that can run the code as described.'''
    
    def __init__(self):
        '''Initialize the computer.'''
        self.register = {'a':0, 'b':0, 'c':0, 'd':0}
        self.program = []
        self.pc = 0
        self.statements_executed = 0

    def load_program(self, program):
        self.program = program
        self.pc = 0

    def resolve(self, value):
        '''Given an instruction argument, decide if it is a
        register reference or an immediate value.'''
        if value in self.register:
            return self.register[value]
        return int(value)

    def execute_statement(self, statement):
        '''Parse the command and execute it.'''
        part = statement.split()
        cmd = part[0]
        if cmd == 'inc':
            self.register[part[1]] += 1
        elif cmd == 'dec':
            self.register[part[1]] -= 1
        elif cmd == 'cpy':
            self.register[part[2]] = self.resolve(part[1])
        elif cmd == 'jnz':
            if self.resolve(part[1]) != 0:
                self.pc += self.resolve(part[2]) - 1
        self.pc += 1
        self.statements_executed += 1

    def run_program(self):
        '''Keep executing statements until the program counter
        reaches past the last statement of the program.'''
        while self.pc < len(self.program):
            self.execute_statement(self.program[self.pc])

if __name__ == '__main__':
    f = open('a12_input.txt', 'r')
    data = []
    for line in f:
       line = line.strip()
       if line:
           data.append(line)
    f.close
    
    bm = bunnymachine()
    bm.load_program(data)
    # Same as version 1, except we have to initialize
    # the 'c' register to 1 instead of zero.
    bm.register['c'] = 1
    bm.run_program()
    print(f"Value of registers: {bm.register}")

