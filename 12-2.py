grid = {}

y = 0
for s in open('12-1.in').readlines():
    x = 0
    for h in list(s.strip()):
        if h == 'S':
            start = (x,y)
            h = 'a'
        elif h == 'E':
            end = (x,y)
            h = 'z'
        grid[(x,y)] = ord(h)-96
        x = x + 1
    y = y + 1

items = []
items.append((0, end))
visited = {}

while len(items) > 0:
    dist, pos = items.pop(0)
    if pos in visited.keys():
        continue
    if grid[pos] == 1:
        print(dist)
        break

    visited[pos] = dist

    _x, _y = pos
    for adj in ((_x,_y+1), (_x,_y-1), (_x+1,_y), (_x-1,_y)):
        try:
            if adj not in visited.keys() and grid[adj] >= grid[pos]-1:
                items.append((dist+1, adj))
        except:
            pass
