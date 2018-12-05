def parse(line):
    splat = line.split(' ')

    idint = int(splat[0][1:])

    x = splat[2][:-1].split(',')

    y = splat[3].split('x')
    return [idint, int(x[0]), int(x[1]), int(y[0]), int(y[1])]


def increment(fabric, x, y, xsize, ysize):
    for i in xrange(xsize):
        for j in xrange(ysize):
            a, b = x + i, y + j
            if a not in fabric:
                fabric[a] = dict()
            thread = fabric[a]
            thread[b] = 1 + thread.get(b, 0)


with open('input-3.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]


fab = dict()

for datum in data:
    [idint, x, y, xsize, ysize] = parse(datum)
    increment(fab, x, y, xsize, ysize)

count = 0
for k in fab:
    for l in fab[k]:
        if fab[k][l] > 1:
            count += 1

print count
