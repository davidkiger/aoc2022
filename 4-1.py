count = 0
for x in open('4-1.in').readlines():
    (a, b) = x.strip().split(',')
    (a_min, a_max) = a.split('-')
    (b_min, b_max) = b.split('-')

    if ((int(a_min) <= int(b_min) and int(a_max) >= int(b_max)) or
        (int(b_min) <= int(a_min) and int(b_max) >= int(a_max))):
        count = count + 1

print(count)
