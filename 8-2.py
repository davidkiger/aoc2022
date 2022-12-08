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
        top_count = 0
        bottom_count = 0
        left_count = 0
        right_count = 0

        for _i in range(i-1, -1, -1):
            top_count = top_count + 1
            if grid[_i][j] >= grid[i][j]: break

        for _i in range(i+1, len(grid)):
            bottom_count = bottom_count + 1
            if grid[_i][j] >= grid[i][j]: break

        for _j in range(j-1, -1, -1):
            left_count = left_count + 1
            if grid[i][_j] >= grid[i][j]: break

        for _j in range(j+1, len(grid[i])):
            right_count = right_count + 1
            if grid[i][_j] >= grid[i][j]: break

        visible[i][j] = top_count * bottom_count * left_count * right_count

print(max(map(max,visible)))
