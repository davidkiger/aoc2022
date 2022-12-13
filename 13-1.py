def compare(a, b):
    for i in range(min(len(a),len(b))):
        is_ordered = None
        if type(a[i]) == list and type(b[i]) == list:
            is_ordered = compare(a[i], b[i])
        elif type(a[i]) == list and not type(b[i]) == list:
            is_ordered = compare(a[i], [b[i]])
        elif not type(a[i]) == list and type(b[i]) == list:
            is_ordered = compare([a[i]], b[i])
        else:
            if a[i] == b[i]:
                pass
            else:
                return a[i] < b[i]

        if is_ordered is not None:
            return is_ordered

    if len(a) == len(b):
        return None
    else:
        return len(a) < len(b)


tmp = []
pairs = []
for s in open('13-1.in').readlines():
    line = s.strip()
    if line:
        tmp.append(line)
    else:
        pairs.append([eval(tmp[0]), eval(tmp[1])])
        tmp = []

tot = 0
for i in range(len(pairs)):
    if compare(pairs[i][0], pairs[i][1]):
        tot += i+1

print(tot)
