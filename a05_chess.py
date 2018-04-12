import hashlib

my_puzzle_input = 'abbhdwsy'
prefix = my_puzzle_input.encode('utf-8')

password = ''
index = 0

while len(password) < 8:
    thishash = hashlib.md5(prefix + str(index).encode('utf-8')).hexdigest()
    if thishash[0:5] == '00000':
        password += thishash[5]
    index += 1

print('Password = {}'.format(password))
