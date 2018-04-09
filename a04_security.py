from collections import namedtuple
from collections import Counter

Code = namedtuple('Code', 'nameparts, sector_id, checksum')

codes = list()

f = open('a04_input.txt')
for line in f:
    line = line.strip('\n')
    if line:
        values = line.split('-')
        nameparts = list()
        sector_id = None
        checksum = None
        for value in values:
            if '[' in value:
                x = value.split('[')
                sector_id = int(x[0])
                checksum = x[1].strip(']')
            else:
                nameparts.append(value)
        codes.append(Code(nameparts, sector_id, checksum))
f.close()

# Approach:
# * Use a Counter() to simplify counting up letters
# * Use .items() to get the key, value tuples out of the dictionary.
# * For a given code, first sort the counted letters alphabetically,
#   then sort by count decending.  .sort() in python is stable, so letters
#   that are tied by frequency stay in their same relative alpha order we
#   established earlier.

sector_sum = 0

for code in codes:
    frequency = Counter()
    for string in code.nameparts:
        for char in string:
            frequency[char] += 1
    ss = sorted(frequency.items(), key=lambda x: x[0]) # sort by letter
    ss.sort(key=lambda x: x[1], reverse=True)  # sort by frequency descending
    string = ''.join([x[0] for x in ss])  # smash letters into one string
    if string[0:5] == code.checksum:
        sector_sum += code.sector_id

print(f'Valid code sector total: {sector_sum}')

        
        

    
