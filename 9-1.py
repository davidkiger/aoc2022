def separated(a, b):
    if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
        return False
    return True
    

x = y = 0
head = (x,y)
tail = (x,y)
visited = set(tail)
for s in open('9-1.in').readlines():
    d, v = s.strip().split()
    if d == "U":
       for i in range(int(v)):
           head = (head[0], head[1]-1)
           if separated(head, tail):
               tail = (head[0], head[1]+1)
               visited.add(tail)
    elif d == "D":
       for i in range(int(v)):
           head = (head[0], head[1]+1)
           if separated(head, tail):
               tail = (head[0], head[1]-1)
               visited.add(tail)
    elif d == "L":
       for i in range(int(v)):
           head = (head[0]-1, head[1])
           if separated(head, tail):
               tail = (head[0]+1, head[1])
               visited.add(tail)
    elif d == "R":
       for i in range(int(v)):
           head = (head[0]+1, head[1])
           if separated(head, tail):
               tail = (head[0]-1, head[1])
               visited.add(tail)

print(len(visited))
