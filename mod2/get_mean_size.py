import sys

def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    count = 0
    for i in range(len(lines)):
        line = lines[i].split()
        count += line[3]
    result = count / len(lines)
    print(result)
    return result