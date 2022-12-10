x = 1
cycle = 1
total = 0
for s in open('10-1.in').readlines():
    tokens = s.strip().split(' ')
    if len(tokens) == 1:
        if (cycle-20) % 40 == 0:
            total = total + (cycle * x)
        cycle = cycle + 1
    elif len(tokens) == 2:
        (i, v) = tokens
        if (cycle-20) % 40 == 0:
            total = total + (cycle * x)
        cycle = cycle + 1

        if (cycle-20) % 40 == 0:
            total = total + (cycle * x)
        cycle = cycle + 1

        x = x + int(v)

print(total)
