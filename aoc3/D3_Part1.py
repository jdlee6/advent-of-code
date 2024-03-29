def read_file(f):
    with open(f, 'r') as f:
        lines = f.readlines()

        dir1 = lines[0].split(',')
        dir1 = [i.strip() for i in dir1]
        # print(dir1)

        dir2 = lines[1].split(',')
        dir2 = [i.strip() for i in dir2]
        # print(dir2)

    return dir1, dir2


def find_coords(direc):
    ''' find every single coordinate and stores in a set ''' 
    x, y = 0, 0
    temp = set()
    
    for pair in direc:
        if pair[0] == 'R':
            for _ in range(int(pair[1:])):
                x += 1
                # print(x,y)
                temp.add((x, y))

        elif pair[0] == 'U':
            for _ in range(int(pair[1:])):
                y += 1
                # print(x,y)
                temp.add((x, y))

        elif pair[0] == 'L':
            for _ in range(int(pair[1:])):
                x -= 1
                # print(x,y)
                temp.add((x, y))

        elif pair[0] == 'D':
            for _ in range(int(pair[1:])):
                y -= 1
                # print(x,y)
                temp.add((x, y))

    return temp


def find_intersections(a, b):
    ''' takes 2 sets and finds intersection '''
    return a.intersection(b)


if __name__ == "__main__":
    # print(read_file('./input.txt')[0])
    # print(read_file('./input.txt')[1])

    # print(find_coords(read_file('./input.txt')[0]))
    # print(find_coords(read_file('./input.txt')[1]))

    # print(find_coords(dir2))
    print(find_intersections(find_coords(read_file('./input.txt')[0]), find_coords(read_file('./input.txt')[1])))