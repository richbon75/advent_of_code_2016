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
# Part 2:
# * Rotate each letter and search for strings with 'north' in them.

sector_sum = 0
valid_codes = list()

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
        valid_codes.append(code)

def decrypt_letter(letter, sector_id):
    """Return the decrypted version of the letter."""
    alpha_offset = ord(letter) - ord('a')  # Results in 'a' = 0, 'z' = 25
    alpha_offset = (alpha_offset + sector_id) % 26
    return chr(ord('a') + alpha_offset)

for code in valid_codes:
    decrypted_string = ''
    for string in code.nameparts:
        for letter in string:
            decrypted_string += decrypt_letter(letter, code.sector_id)
        decrypted_string += ' '
    decrypted_string = decrypted_string.strip()
    if 'north' in decrypted_string:
        print(f'{decrypted_string} -- {code.sector_id}')


        
        

    
