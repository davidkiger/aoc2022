from functools import cmp_to_key

def compare(a, b):
    for i in range(min(len(a),len(b))):
        is_ordered = 0
        if type(a[i]) == list and type(b[i]) == list:
            is_ordered = compare(a[i], b[i])
        elif type(a[i]) == list and not type(b[i]) == list:
            is_ordered = compare(a[i], [b[i]])
        elif not type(a[i]) == list and type(b[i]) == list:
            is_ordered = compare([a[i]], b[i])
        else:
            if a[i] == b[i]:
                pass
            elif a[i] < b[i]:
                return -1
            else:
                return 1

        if is_ordered:
            return is_ordered

    if len(a) == len(b):
        return 0
    elif len(a) < len(b):
        return -1
    else:
        return 1


packets = []
for s in open('13-1.in').readlines():
    line = s.strip()
    if line:
        packets.append(eval(line))

packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare))

first = 0
for i in range(len(packets)):
    if packets[i] == [[2]]:
        first = i+1
    if packets[i] == [[6]]:
        print( first * (i+1) )
        exit()
