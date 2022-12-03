import string

alpha = list(string.ascii_lowercase)
alpha.extend(string.ascii_uppercase)
translation = {}
val = 1
for x in alpha:
    translation[x] = val
    val = val + 1

priority = 0
for x in open('3-1.in').readlines():
    x = x.strip()
    matches = set()
    s1 = x[:len(x)//2]
    s2 = x[len(x)//2:]

    for l in list(s1):
        if l in s2:
            matches.add(l)
 
    for l in matches:
        priority = priority + translation[l]

print(priority)
