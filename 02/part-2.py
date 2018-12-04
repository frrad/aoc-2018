with open('input-2.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]


def find_mask(data):
    masks = set()
    for idstr in data:
        tomask = list(idstr)
        for i in xrange(len(idstr)):
            mask = ''.join(
                [tomask[j] if i != j else '*' for j in xrange(len(idstr))])
            if mask in masks:
                return mask
            masks.add(mask)


print ''.join([l for l in list(find_mask(data)) if l != '*'])
