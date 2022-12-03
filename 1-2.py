max_cal = []
tot = 0
for x in open('1-1.in').readlines():
    x = x.strip()

    if x == '':
        max_cal.append(tot)
        tot = 0
    else:
        tot = tot + int(x)

max_cal.sort()
print(sum(max_cal[-3:]))
