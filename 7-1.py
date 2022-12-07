class Dir:
  def __init__(self, name, parent = None):
    self.name = name
    self.files = {}
    self.dirs = {}
    self.parent = parent

def walk_dir(d, prefix, print_it = False):
    this_size = 0
    path = prefix + d.name
    if print_it:
        print(path)

    for x in d.dirs.keys():
        this_size = this_size + walk_dir(d.dirs[x], path + '/', print_it)

    for x in d.files.keys():
        if print_it:
            print(path + '/' + x + ' - ' + d.files[x])
        this_size = this_size + int(d.files[x])

    dir_sizes[path] = this_size
    return this_size

lines = []
for s in open('7-1.in').readlines():
    lines.append(s.strip())

dir_sizes = {}
root = Dir("")
current = root
for idx in range(1, len(lines)):
    s = lines[idx]
    tokens = s.split(' ')

    if tokens[0] == '$':
        if tokens[1] == 'ls':
            cont = True
            next_idx = idx
            while cont:
                next_idx = next_idx + 1
                try:
                    check = lines[next_idx]
                except:
                    break
                if check[0] != '$':
                    (a, b) = check.split(' ')
                    if a == 'dir':
                        current.dirs[b] = (Dir(b, current))
                    else:
                        current.files[b] = a
                else:
                    cont = False
        elif tokens[1] == 'cd':
            if tokens[2] == '..':
                current = current.parent
            else:
                if tokens[2] not in current.dirs.keys():
                    current.dirs[tokens[2]] = (Dir(tokens[2], current))
                current = current.dirs[tokens[2]]

walk_dir(root, '')

total = 0
for d in dir_sizes.keys():
    if dir_sizes[d] <= 100000:
        total = total + dir_sizes[d]

print(total)
