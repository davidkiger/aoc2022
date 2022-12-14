def drop_sand():
    sand = [0,500]
    stopped = False
    while not stopped:
        if ground[sand[0]+1][sand[1]] == '.':
            sand[0] += 1
        elif ground[sand[0]+1][sand[1]] == 'o' or ground[sand[0]+1][sand[1]] == '#':
            if ground[sand[0]+1][sand[1]-1] == 'o' or ground[sand[0]+1][sand[1]-1] == '#':
                if ground[sand[0]+1][sand[1]+1] == 'o' or ground[sand[0]+1][sand[1]+1] == '#':
                    stopped = True
                else:
                    sand[0] += 1
                    sand[1] += 1
            else:
                sand[0] += 1
                sand[1] -= 1
        else:
            stopped = True
    ground[sand[0]][sand[1]] = 'o'


ground = [['.' for i in range(1000)] for j in range(1000)]
ground[0][500] = '+'
pos = [[500, 0]]

for s in open('14-1.in').readlines():
    points = s.strip().split(' -> ')
    prev = None
    for p in points:
        x, y = list(map(int, p.strip().split(',')))
        if not prev:
            prev = (x,y)
        else:
            if prev[0] == x: # vertical line
                for i in range(min(y,prev[1]), max(y,prev[1])+1):
                    ground[i][x] = '#'
            elif prev[1] == y: # horizontal line
                for i in range(min(x,prev[0]), max(x,prev[0])+1):
                    ground[y][i] = '#'
            else:
                print(f'shit. {prev} {x},{y}')

            prev = (x,y)

count = 0
while True:
    try:
        drop_sand()
        count += 1
    except:
        print(count)
        break

# for j in range(0, 15):
#    print(''.join(ground[j][475:510]))
