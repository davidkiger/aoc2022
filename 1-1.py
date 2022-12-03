max_cal = 0
tot = 0
for x in open('1-1.in').readlines():
    x = x.strip()

    if x == '':
        if tot > max_cal:
            max_cal = tot
        tot = 0
    else:
        tot = tot + int(x)

print(max_cal)
