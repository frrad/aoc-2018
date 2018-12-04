with open('input-1.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

inted = []

for x in data:
    y = int(x[1:])
    if x[0] == '-':
        y *= -1

    inted.append(y)


curr = 0
seen = set()
i = 0
length = len(inted)

while True:
    if curr in seen:
        print curr
        break

    seen.add(curr)
    curr += inted[i % length]
    i += 1
