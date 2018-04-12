import hashlib

my_puzzle_input = 'abbhdwsy'
prefix = my_puzzle_input.encode('utf-8')

password = [None] * 8
index = 0

while True:
    thishash = hashlib.md5(prefix + str(index).encode('utf-8')).hexdigest()
    if thishash[0:5] == '00000':
        if (thishash[5] >= '0' and thishash[5] <= '7'
            and password[int(thishash[5])] is None):
            password[int(thishash[5])] = thishash[6]
            if None not in password:
                break
    index += 1

print('Password = {}'.format(''.join(password)))
