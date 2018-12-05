def cancels(a,b):
    return a.lower() == b.lower() and a !=b

    

def react(inlist):
    from_ptr, to_ptr = 0,0
    while from_ptr < len(inlist):
        while from_ptr +1 < len(inlist) and cancels( inlist[from_ptr], inlist[from_ptr+1]):
            from_ptr +=2

        if from_ptr >= len(inlist):
            break
        inlist[to_ptr] = inlist[from_ptr]
        to_ptr += 1
        from_ptr +=1

    return inlist[:to_ptr]

def stabilize(inlist):
    lastlen = 0
    while len(inlist) != lastlen:
        lastlen = len(inlist)
        inlist = react(inlist)

    return inlist

with open('input-5.txt', 'r') as f:
    data = [l.strip() for l in f.readlines()]

enzyme = list(data[0])
print len( stabilize(enzyme))


