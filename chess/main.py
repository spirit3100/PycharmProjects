from logic_chess import *


def main():

    print()
    desk = show_desk(create_desk())
    while True:
        cage_1 = step('your figure position: ')
        f_desk, steps = find_figure(desk, cage_1)
        print(f'permission steps: {steps}')
        cage_2 = step('your step: ')
        update_desk(desk, player_step, (cage_1, cage_2))
        if cage_1 == 'exit' or cage_2 == 'exit': break


main()
