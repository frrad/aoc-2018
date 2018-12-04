def frequencies(string):
    freqs = dict()
    for l in string:
        freqs[l] = 1 + freqs.get(l, 0)

    return freqs


def twos_threes(fr):
    twos = []
    threes = []
    for key in fr:
        val = fr[key]
        if val == 2:
            twos.append(key)
        if val == 3:
            threes.append(key)

    return twos, threes


with open('input-2.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

a, b = 0, 0
for string in data:
    tw, th = twos_threes(frequencies(string))
    if len(tw) > 0:
        a += 1
    if len(th) > 0:
        b += 1

print a * b
