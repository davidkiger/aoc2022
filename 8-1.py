grid = []
for s in open('8-1.in').readlines():
    grid.append([int(x) for x in list(s.strip())])

visible = []
for i in range(0, len(grid)):
    visible.append([])
    for j in range(0, len(grid[i])):
        visible[i].append(False)

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1:
            visible[i][j] = True
        else:
            from_top = True
            from_left = True
            from_bottom = True
            from_right = True

            for _i in range(0, i):
                if grid[_i][j] >= grid[i][j]: from_top = False
            for _i in range(i+1, len(grid)):
                if grid[_i][j] >= grid[i][j]: from_bottom = False
            for _j in range(0, j):
                if grid[i][_j] >= grid[i][j]: from_left = False
            for _j in range(j+1, len(grid[i])):
                if grid[i][_j] >= grid[i][j]: from_right = False

            if from_top or from_left or from_bottom or from_right:
                visible[i][j] = True

print(sum([x.count(True) for x in visible]))
