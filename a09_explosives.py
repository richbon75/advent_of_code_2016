
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
    if not repeater_end:
        raise ValueError(f'Bad repeater at position {pointer}')
    repeater = data[pointer+1:repeater_end].split('x')
    output_string = data[repeater_end+1:repeater_end+1+int(repeater[0])]*int(repeater[1])
    return repeater_end+1+int(repeater[0]), output_string

def decompressor(data):
    decompressed = ''
    pointer = 0
    while pointer < len(data):
        pointer, substring = scan_to_repeater(data, pointer)
        decompressed += substring
        pointer, substring = apply_repeater(data, pointer)
        decompressed += substring
    return decompressed

new_data = decompressor(data)
print(f'Length of uncompressed data = {len(new_data)}')

