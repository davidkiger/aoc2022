count = 0
stacks = [[],[],[],[],[],[],[],[],[]]
for x in open('5-1.in').readlines():
    if count < 8:
        if x[0] == '[': stacks[0].append(x[1])
        if x[4] == '[': stacks[1].append(x[5])
        if x[8] == '[': stacks[2].append(x[9])
        if x[12] == '[': stacks[3].append(x[13])
        if x[16] == '[': stacks[4].append(x[17])
        if x[20] == '[': stacks[5].append(x[21])
        if x[24] == '[': stacks[6].append(x[25])
        if x[28] == '[': stacks[7].append(x[29])
        if x[32] == '[': stacks[8].append(x[33])
        count = count + 1
    else:
        if x[0] == 'm':
            (_z, c, _z, f, _z, t) = x.strip().split(' ')
            moves = 0
            while moves < int(c):
                box = stacks[int(f)-1].pop(0)
                stacks[int(t)-1].insert(0, box)
                moves = moves + 1

print(stacks[0][0]+stacks[1][0]+stacks[2][0]+stacks[3][0]+stacks[4][0]+stacks[5][0]+stacks[6][0]+stacks[7][0]+stacks[8][0])
