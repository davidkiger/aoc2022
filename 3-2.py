import string

alpha = list(string.ascii_lowercase)
alpha.extend(string.ascii_uppercase)
translation = {}
val = 1
for x in alpha:
    translation[x] = val
    val = val + 1

priority = 0
badges = []
for x in open('3-1.in').readlines():
    x = x.strip()
    badges.append(x)

    if len(badges) == 3:
        matches = set()

        for l in list(badges[0]):
            if l in badges[1] and l in badges[2]:
                priority = priority + translation[l]
                break

        badges = []

print(priority)
