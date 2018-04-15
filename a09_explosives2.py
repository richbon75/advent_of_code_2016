

f = open('a09_input.txt','r')

data = None

for line in f:
    line = line.strip()
    if line:
        data = line
   
f.close()

def scan_to_repeater(data, pointer):
    '''Scans the string to the start of the next repeater.
    Returns:  updated pointer, string_length'''
    start = pointer
    while pointer < len(data) and data[pointer] != '(':
        pointer += 1
    return pointer, pointer-start

def apply_repeater(data, pointer):
    '''Assumes pointer is positioned at start of a repeater rule ex: (3x4)
    Returns: updated pointer, string_length'''
    repeater_end = data.find(')',pointer)
    if pointer >= len(data):
        return pointer, None
    if not repeater_end or data[pointer] != '(':
        raise ValueError(f'Bad repeater at position {pointer}')
    repeater = data[pointer+1:repeater_end].split('x')
    substring = data[repeater_end+1:repeater_end+1+int(repeater[0])]
    # Here we recurse - find the length of the substring, if it were decompresesd.
    decompressed_length = decompressor(substring)
    output_length = decompressed_length * int(repeater[1])
    return repeater_end+1+int(repeater[0]), output_length

def decompressor(data):
    """Return only the length of the uncompressed data"""
    decompressed_length = 0
    pointer = 0
    while pointer < len(data):
        pointer, substring_length = scan_to_repeater(data, pointer)
        if substring_length:
            decompressed_length += substring_length
        pointer, substring_length = apply_repeater(data, pointer)
        if substring_length:
            decompressed_length += substring_length
    return decompressed_length

new_data_length = decompressor(data)
print(f'Length of uncompressed data = {new_data_length}')

