from data_chess import *

def blank_desk():

    s = {}
    for i in vertical:
        for v in horizontal: s[i + str(v)] = (vertical.index(i) , horizontal.index(v)), None, '  ', None

    return s

def knight(desk, cage_x_y):

    x = cage_x_y[1]
    a, b, c, d = x[0] + 2, x[0] - 2, x[1] + 1, x[1] - 1
    e, f, h, g = x[0] + 1, x[0] - 1, x[1] + 2, x[1] - 2
    steps = [(a, c), (e, h), (a, d), (e, g), (f, g), (b, d), (b, c), (f, h)]

    return find_permission(steps)

def find_permission(list_x_y, reverse=0):

    blank_d = blank_desk()
    new_l = []
    l = []
    # print(f'list: {list_x_y}')
    [l.append(i) for i in list_x_y if i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7]
    [new_l.append(i) for i, k in blank_d.items() if k[0] in l]
    if reverse == -1: new_l.reverse()
    # print(f'new l: {new_l}')
    return new_l

def rook(desk, cage_x_y):

    step = []
    x = cage_x_y[1]
    f = ((0, 1, 0),(0, -1, -1),(1, 0, 0),(-1, 0, -1))
    def find_pos(desk, b=0, c=0, d=0):
        new_list = []
        modify_list = []
        a = 0
        a2 = 0
        for i in range(1, 8):
            a += b
            a2 += c
            new_list.append((x[0] + a, x[1] + a2))
        if d == -1: list = find_permission(new_list, reverse=-1)
        else: list = find_permission(new_list)
        for i in list:
            if desk.get(i)[1] != None:
                modify_list.append(i)
                break
            else:
                modify_list.append(i)

        return modify_list

    for i in f: step.extend(find_pos(desk, b=i[0], c=i[1], d=i[2]))
    # print(f's4 {step}')

    return step

def bishop(desk, cage_x_y):

    def find(list_s, x_y, int_1, int_2):

        x, y = x_y
        for i in range(8):
            x += int_1
            y += int_2
            list_s.append((x, y))

        return list_s

    x_y = cage_x_y[1]
    steps = []
    x = ((1,1), (-1,-1), (-1,1), (1,-1))
    for i in x: steps = find(steps, x_y, i[0], i[1])

    return find_permission(steps)

def queen(desk, cage_x_y):

    a = rook(desk, cage_x_y)
    b = bishop(desk, cage_x_y)

    return a + b

def king(desk, cage_x_y):

    x = cage_x_y[1]
    a, b, c, d = x[0] + 1, x[0] -1, x[1] + 1, x[1] - 1
    steps = [(a, c), (b, c), (a, d), (b, d), (x[0], c), (x[0], d), (a, x[1]), (b, x[1])]

    return find_permission(steps)

def pawns(desk, cage_x_y):

    cage, (x, y) = cage_x_y
    steps = []
    color = desk.get(cage)[3]
    x_y = desk.get(cage)[0]
    if color == 'white':
        steps = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        if x_y[1] == 1: steps.append((x, y + 2))
    elif color == 'black':
        steps = [(x, y - 1), (x - 1, y - 1), (x + 1, y - 1)]
        if x_y[1] == 6: steps.append((x, y - 2))

    return find_permission(steps)
