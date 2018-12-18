def get_input(filename):
    with open(filename, 'r') as f:
        data = [l.strip() for l in f.readlines()]
    return data


def show(array):
    return '\n'.join([''.join(line) for line in array])


def surrounds(array, i, j):
    ans = dict()

    hw = len(array)

    for a in range(-1, 2):
        for b in range(-1, 2):
            x, y = a + i, b + j
            if x < 0 or x > hw - 1:
                continue
            if y < 0 or y > hw - 1:
                continue
            if a == 0 and b == 0:
                continue

            item = array[x][y]
            ans[item] = ans.get(item, 0) + 1

    return ans


def evolve(array):
    ans = []
    hw = len(array)

    for i in xrange(hw):
        ans.append(['z'] * hw)
        for j in xrange(hw):
            this = array[i][j]
            surroundings = surrounds(array, i, j)

            if this == '.':
                if surroundings.get('|', 0) >= 3:
                    ans[i][j] = '|'
                else:
                    ans[i][j] = '.'
                continue
            if this == '|':
                if surroundings.get('#', 0) >= 3:
                    ans[i][j] = '#'
                else:
                    ans[i][j] = '|'
                continue
            if this == '#':
                if surroundings.get('#', 0) < 1 or surroundings.get('|', 0) < 1:
                    ans[i][j] = '.'
                else:
                    ans[i][j] = '#'
                continue

    return ans


in_state = get_input('input-18.txt')
state_arr = [list(line) for line in in_state]


after_n_minutes = 10
for i in xrange(1, after_n_minutes + 1):
    state_arr = evolve(state_arr)

counts = dict()
for i in xrange(len(state_arr)):
    for j in xrange(len(state_arr)):
        char = state_arr[i][j]
        counts[char] = counts.get(char, 0) + 1

print counts.get('#', 0) * counts.get('|', 0)
