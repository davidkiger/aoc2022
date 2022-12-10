x = 1
cycle = 1
crt = ''
for s in open('10-1.in').readlines():
    tokens = s.strip().split(' ')
    if len(tokens) == 1:
        if x-1 <= (cycle-1)%40 <= x+1: crt = crt + '#'
        else: crt = crt + '.'
        cycle = cycle + 1
    elif len(tokens) == 2:
        if x-1 <= (cycle-1)%40 <= x+1: crt = crt + '#'
        else: crt = crt + '.'
        cycle = cycle + 1

        if x-1 <= (cycle-1)%40 <= x+1: crt = crt + '#'
        else: crt = crt + '.'
        cycle = cycle + 1

        x = x + int(tokens[1])

print(crt[0:40])
print(crt[40:80])
print(crt[80:120])
print(crt[120:160])
print(crt[160:200])
print(crt[200:240])
