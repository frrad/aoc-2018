def get_input(filename):
    with open(filename, 'r') as f:
        data = [l.strip() for l in f.readlines()]
    return data


def parse_time(timestr):
    year = int(timestr[1:5])
    month = int(timestr[6:8])
    day = int(timestr[9:11])

    hour = int(timestr[12:14])
    minute = int(timestr[15:17])

    return year, month, day, hour, minute


def parse(line):
    left = line[:18]
    right = line[19:]

    time = parse_time(left)

    return time, right


data = get_input('input-4.txt')
data.sort()


for line in data:
    print line
    print parse(line)
