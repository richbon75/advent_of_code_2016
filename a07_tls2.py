
from collections import deque

values = list()

f = open('a07_input.txt','r')
for line in f:
    line = line.strip('\n').strip()
    if line:
        values.append(line)
f.close()

def chopper(string):
    results = {'outer_sections':[], 'inner_sections':[]}
    while '[' in string:
        loc = string.find('[')
        end = string.find(']')
        results['outer_sections'].append(string[0:loc])
        results['inner_sections'].append(string[loc+1:end])
        string = string[end+1:]
    if string:
        results['outer_sections'].append(string)
    return results

def supports_ssl(string):
    parts = chopper(string)
    for section in parts['outer_sections']:
        for i in range(len(section)-2):
            if section[i] != section[i+1] and section[i] == section[i+2]:
                pattern = section[i+1] + section[i] + section[i+1]
                for inner in parts['inner_sections']:
                    if pattern in inner:
                        # print(f'matched pattern: {pattern}')
                        return True
    return False


support_count = 0
for value in values:
    if supports_ssl(value):
        support_count += 1

print(f'Number supporting ssl: {support_count}')


