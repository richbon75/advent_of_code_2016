
class Warehouse(object):
    def __init__(self):
        self.robots = dict()
        self.outputs = dict()

    def assign_value(self, dest, rule, value):
        if dest == 'bot':
            if rule not in self.robots:
                self.robots[rule] = Robot(rule, self)
            self.robots[rule].receive_chip(value)
        else:
            if rule not in self.outputs:
                self.outputs[rule] = []
            self.outputs[rule].append(value)

    def assign_rules(self, robot, lowdest, lowrule, highdest, highrule):
        if robot not in self.robots:
            self.robots[robot] = Robot(robot, self)
        if lowdest == 'bot' and lowrule not in self.robots:
            self.robots[lowrule] = Robot(lowrule, self)
        if highdest == 'bot' and highrule not in self.robots:
            self.robots[highrule] = Robot(highrule, self)
        self.robots[robot].lowdest = lowdest
        self.robots[robot].lowrule = lowrule
        self.robots[robot].highdest = highdest
        self.robots[robot].highrule = highrule             

class Robot(object):
    def __init__(self, myname, warehouse):
        self.myname = myname
        self.lowdest = None
        self.lowrule = None
        self.highdest = None
        self.highrule = None
        self.chips = []
        self.warehouse = warehouse

    def __str__(self):
        return f'Robot {self.myname} has chips: {self.chips}'

    def __repr__(self):
        return self.__str__()

    def receive_chip(self, value):
        if len(self.chips) > 1:
            raise ValueError(f'Robot {self.myname} is already holding the maximum number of chips.')
        self.chips.append(value)
        self.chips.sort()  # makes sure the lower value is in slot [0]
        if len(self.chips) == 2:
            if self.chips == [17, 61]:  # Find answer for Part 1.
                print(f'Part 1 output: I HAVE THE MAGIC CHIPS: {self}')
            self.give_chips()

    def give_chips(self):
        '''Happens if a robot has two chips'''
        lowchip, highchip = self.chips
        self.chips.clear()
        self.warehouse.assign_value(self.lowdest, self.lowrule, lowchip)
        self.warehouse.assign_value(self.highdest, self.highrule, highchip)

# Seems like we should save processing the initial "value x goes to bot y"
# commands until we have all the rules set up, so hold them in initial_values
initial_values = list()
w = Warehouse()

with open('a10_input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        words = line.split()
        if words[0] == 'value':
            initial_values.append((int(words[5]), int(words[1])))
        else:
            w.assign_rules(int(words[1]), words[5], int(words[6]), words[10], int(words[11]))

for x in initial_values:
    w.assign_value('bot', x[0], x[1])

part2_output = w.outputs[0][0] * w.outputs[1][0] * w.outputs[2][0]
print(f'Part 2 output: {part2_output}')
