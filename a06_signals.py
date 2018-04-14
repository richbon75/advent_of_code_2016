from collections import Counter

values = []

f = open('a06_input.txt','r')
for line in f:
    line = line.strip().strip('\n')
    if line:
        values.append(list(line))
f.close()

transposed = [x for x in zip(*values)]

output = ''

for place in transposed:
    frequency=Counter()
    for letter in place:
        frequency[letter] += 1
    results = list(frequency.items())
    results.sort(key=lambda x: x[1])
    results.reverse()
    output += results[0][0]

print(output)



    
