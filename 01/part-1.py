with open('input-1.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

ans = 0
for x in data:
    y = int(x[1:])
    if x[0] == '-':
        y *= -1
    ans += y

print ans
