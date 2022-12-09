def separated(a, b):
    if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
        return False
    return True


def move(head, tail):
    new_x = tail[0]
    new_y = tail[1]

    if head[1] < tail[1]:
        new_y = new_y-1
    elif head[1] > tail[1]:
        new_y = new_y+1

    if head[0] > tail[0]:
        new_x = new_x+1
    elif head[0] < tail[0]:
        new_x = new_x-1

    return (new_x, new_y)

x = y = 0
snake = []
for i in range(10):
    snake.append((x,y))

visited = set()
for s in open('9-1.in').readlines():
    d, v = s.strip().split()
    for j in range(int(v)):
        if d == "U":
            snake[0] = (snake[0][0], snake[0][1]-1)
        elif d == "D":
            snake[0] = (snake[0][0], snake[0][1]+1)
        elif d == "L":
            snake[0] = (snake[0][0]-1, snake[0][1])
        elif d == "R":
            snake[0] = (snake[0][0]+1, snake[0][1])

        for i in range(1,10):
            if separated(snake[i-1], snake[i]):
                snake[i] = move(snake[i-1], snake[i])
        visited.add(snake[9])

print(len(visited))
