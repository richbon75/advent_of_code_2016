
# This is an interim version - it can handle nested decompression,
# but since it generates the FULL STRING, it probably won't solve
# the full input because of space (it would be like 11 gigabytes long)

f = open('a09_input.txt','r')

data = None

for line in f:
    line = line.strip()
    if line:
        data = line
   
f.close()

def scan_to_repeater(data, pointer):
    '''Scans the string to the start of the next repeater.
    Returns:  updated pointer, string'''
    start = pointer
    while pointer < len(data) and data[pointer] != '(':
        pointer += 1
    return pointer, data[start:pointer]

def apply_repeater(data, pointer):
    '''Assumes pointer is positioned at start of a repeater rule ex: (3x4)
    Returns: updated pointer, string'''
    repeater_end = data.find(')',pointer)
    if pointer >= len(data):
        return pointer, None
    if not repeater_end or data[pointer] != '(':
        raise ValueError(f'Bad repeater at position {pointer}')
    repeater = data[pointer+1:repeater_end].split('x')
    substring = data[repeater_end+1:repeater_end+1+int(repeater[0])]
    # Recurse here - decompress the substring before multiplying it
    substring = decompressor(substring)
    output_string = substring * int(repeater[1])
    return repeater_end+1+int(repeater[0]), output_string

def decompressor(data):
    decompressed = ''
    pointer = 0
    while pointer < len(data):
        pointer, substring = scan_to_repeater(data, pointer)
        if substring:
            decompressed += substring
        pointer, substring = apply_repeater(data, pointer)
        if substring:
            decompressed += substring
    return decompressed

# new_data = decompressor(data)
# print(f'Length of uncompressed data = {len(new_data)}')

# solving test cases from the problem to make sure it works properly
assert len(decompressor('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')) == 445
assert len(decompressor('(27x12)(20x12)(13x14)(7x10)(1x12)A')) == 241920
print('tests passed')

