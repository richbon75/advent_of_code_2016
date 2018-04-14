
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

def supports_tls(string):
    parts = chopper(string)
    abba_inner = False
    abba_outer = False
    for section in parts['outer_sections']:
        for i in range(len(section)-3):
            if (section[i] != section[i+1] and
                section[i:i+2] == section[i+3:i+1:-1]):
                abba_outer = True
    for section in parts['inner_sections']:
        for i in range(len(section)-3):
            if (section[i] != section[i+1] and
                section[i:i+2] == section[i+3:i+1:-1]):
                abba_inner = True
    if abba_outer and not abba_inner:
        return True
    return False

support_count = 0
for value in values:
    if supports_tls(value):
        support_count += 1

print(f'Number supporting tls: {support_count}')
