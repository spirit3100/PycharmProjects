from func_figures import *
from data_chess import *


figures_w_b = {'king': (9818, 9812, lambda: king),
            'queen': (9819, 9813, lambda: queen),
            'bishop': (9821, 9815, lambda: bishop),
            'knight': (9822, 9816, lambda: knight),
            'rook': (9820, 9814, lambda: rook),
            'pawns': (9823, 9817, lambda: pawns)}

def create_desk():

    desk = filling_desk(blank_desk(), 1, 2)
    desk = filling_desk(desk, 8, 7, 1)

    return desk

def filling_desk(desk, rowFig, rowPawns, color = 0):

    for i in range(0, len(vertical)):
        desk[vertical[i] + str(rowFig)] = desk.get(vertical[i] + str(rowFig))[0], figure_name[i], chr(figures_w_b[figure_name[i]][color]), color_figure[color]
    a = [i + str(rowPawns) for i in vertical]
    for i in a:
        desk[i] = desk.get(i)[0], 'pawns', chr(figures_w_b['pawns'][color]), color_figure[color]

    return desk

def update_desk(desk, first, steps):

    global player_step
    if first == 'black': player_step = color_figure[0]
    elif first == 'white': player_step = color_figure[1]
    step_A, step_B = steps
    if step_A != step_B:
        if first == 'white':
            if desk.get(step_B)[2] != '  ':
                broken_pieces[0].append(desk.get(step_B)[2])
        elif first == 'black':
            if desk.get(step_B)[2] != '  ':
                broken_pieces[1].append(desk.get(step_B)[2])
        desk[step_B] = (desk.get(step_B)[0], desk.get(step_A)[1], desk.get(step_A)[2], desk.get(step_A)[3])
        desk[step_A] = (desk[step_A][0], None, '  ', None)
    if broken_pieces[0]: print(f'white user {broken_pieces[0]}')
    if broken_pieces[1]: print(f'black user {broken_pieces[1]}')
    show_desk(desk)

    return desk

def show_desk(desk):

    # print(f'show {add_desk}')
    count = 0
    for i, k in desk.items():
        print(f' | {k[2]}', end='')
        count += 1
        if count == 8:
            print(f' |  {i[:1]}\n ---------------------------------------')
            count = 0
    print(f'   1    2    3    4    5    6    7    8\n')
    print(f'{player_step} step')

    return desk

def find_figure(desk, cage):

    s = blank_desk()
    x_y = s.get(cage)
    get_figure = desk.get(cage)[1]
    cage_x_y = cage, x_y[0]
    step = figures_w_b.get(get_figure)[2]()(desk, cage_x_y)
    return desk, step

def find(list_s, y):

    l = []
    for k in list_s:
        if k[0] >= 0 and k[0] <= 7 and k[1] >= 0 and k[1] <= 7:
            l.append(k)
    if y in l: return True
    else: return False

def step(str):

    desk = blank_desk()
    while True:
        cage = input(str)
        if cage == 'exit' or desk.get(cage):
            break
        elif not desk.get(cage):
            continue
    return cage
