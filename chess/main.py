from logic_chess import *


def main():

    s = create_desk()
    print()
    f = show_desk(s)
    while True:
        a = step('your figure position: ')
        f_d, st = find_figure(f, a)
        print(f'permission steps: {st}')
        b = step('your step: ')
        update_desk(f, player_step, (a, b))
        if a == 'exit' or b == 'exit': break


main()
