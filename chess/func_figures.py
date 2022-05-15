from data_chess import *

def blank_desk():

    s = {}
    for i in vertical:
        for v in horizontal:
            s[i + str(v)] = (vertical.index(i) , horizontal.index(v)), None, '  ', None

    return s

def knight(desk, cage_x_y):

    x = cage_x_y[1]
    a, b, c, d = x[0] + 2, x[0] - 2, x[1] + 1, x[1] - 1
    e, f, h, g = x[0] + 1, x[0] - 1, x[1] + 2, x[1] - 2
    steps = [(a, c), (e, h), (a, d), (e, g), (f, g), (b, d), (b, c), (f, h)]

    return find_permission(steps)

def find_permission(list_x_y):

    blank_d = blank_desk()
    new_l = []
    l = []
    [l.append(i) for i in list_x_y if i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7]
    [new_l.append(i) for i, k in blank_d.items() if k[0] in l]

    return new_l

def rook(desk, cage_x_y):

    x = cage_x_y[1]
    a = []
    for i in range(-8, 8):
        if x[0] + i >= 0 and x[0] + i < 8:
            c = x[0] + i
            v = x[1]
            a.append((c, v))
        if x[1] + i >= 0 and x[1] + i < 8:
            c = x[0]
            v = x[1] + i
            a.append((c,v))

    return find_permission(a)

def bishop(desk, cage_x_y):

    x_y = cage_x_y[1]
    steps = []
    x = ((1,1), (-1,-1), (-1,1), (1,-1))
    for i in x: steps = bish_find(steps, x_y, i[0], i[1])

    return find_permission(steps)

def bish_find(list_s, x_y, int_1, int_2):

    x, y = x_y
    for i in range(8):
        x += int_1
        y += int_2
        list_s.append((x, y))

    return list_s

def queen(desk, cage_x_y):

    a = rook(desk, cage_x_y)
    b = bishop(desk, cage_x_y)

    return a + b

def king(desk, x_y):

    x = x_y[1]
    a, b, c, d = x[0] + 1, x[0] -1, x[1] + 1, x[1] - 1
    steps = [(a, c), (b, c), (a, d), (b, d), (x[0], c), (x[0], d), (a, x[1]), (b, x[1])]

    return find_permission(steps)

def pawns(desk, cage_x_y):

    cage, (x, y) = cage_x_y
    steps = []
    color = desk.get(cage)[3]
    if color == 'white':
        steps = [(x, y + 1), (x, y + 2), (x - 1, y + 1), (x + 1, y + 1)]
    elif color == 'black':
        steps = [(x, y - 1), (x, y - 2), (x - 1, y - 1), (x + 1, y - 1)]

    return find_permission(steps)
