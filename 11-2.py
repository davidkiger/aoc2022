'''
Monkey 0:
  Starting items: 52, 78, 79, 63, 51, 94
  Operation: new = old * 13
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 1:
  Starting items: 77, 94, 70, 83, 53
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 2:
  Starting items: 98, 50, 76
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 3:
  Starting items: 92, 91, 61, 75, 99, 63, 84, 69
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 4:
  Starting items: 51, 53, 83, 52
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 76, 76
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 75, 59, 93, 69, 76, 96, 65
  Operation: new = old * 19
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 7:
  Starting items: 89
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 4
'''

items = []
items.append([52,78,79,63,51,94])
items.append([77,94,70,83,53])
items.append([98,50,76])
items.append([92,91,61,75,99,63,84,69])
items.append([51,53,83,52])
items.append([76,76])
items.append([75,59,93,69,76,96,65])
items.append([89])

counts = []
for r in range(len(items)):
    counts.append(0)

worry_factor = 5 * 7 * 13 * 11 * 3 * 2 * 17 * 19
for r in range(10000):
    for m in range(8):
        for i in items[m]:
            if m == 0:
                i = (i * 13)
                if i % 5 == 0: items[1].append(i % worry_factor)
                else:          items[6].append(i % worry_factor)
            elif m == 1:
                i = (i + 3)
                if i % 7 == 0: items[5].append(i % worry_factor)
                else:          items[3].append(i % worry_factor)
            elif m == 2:
                i = (i * i)
                if i % 13 == 0: items[0].append(i % worry_factor)
                else:           items[6].append(i % worry_factor)
            elif m == 3:
                i = (i + 5)
                if i % 11 == 0: items[5].append(i % worry_factor)
                else:           items[7].append(i % worry_factor)
            elif m == 4:
                i = (i + 7)
                if i % 3 == 0: items[2].append(i % worry_factor)
                else:          items[0].append(i % worry_factor)
            elif m == 5:
                i = (i + 4)
                if i % 2 == 0: items[4].append(i % worry_factor)
                else:          items[7].append(i % worry_factor)
            elif m == 6:
                i = (i * 19)
                if i % 17 == 0: items[1].append(i % worry_factor)
                else:           items[3].append(i % worry_factor)
            elif m == 7:
                i = (i + 2)
                if i % 19 == 0: items[2].append(i % worry_factor)
                else:           items[4].append(i % worry_factor)

        counts[m] = counts[m] + len(items[m])
        items[m] = []

counts.sort()
print(counts[-1] * counts[-2])
