score = 0
for x in open('2-1.in').readlines():
    (opp, me) = x.strip().split(' ')

    if me == 'X': score = score + 1
    elif me == 'Y': score = score + 2
    elif me == 'Z': score = score + 3

    if opp == 'A':
        if me == 'X': score = score + 3
        elif me == 'Y': score = score + 6
    elif opp == 'B':
        if me == 'Y': score = score + 3
        elif me == 'Z': score = score + 6
    elif opp == 'C':
        if me == 'Z': score = score + 3
        elif me == 'X': score = score + 6

print(score)
