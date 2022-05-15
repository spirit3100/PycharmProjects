from logic_chess import *
# игра в шахматы

# при первом выборе ячейки, идет проверка  на все возможные варианты хода фигуры этой ячейки и выводится на экран.
# при втором выборе ячейки, происводится шаг фигурой.
#
# дальнейшие действия: запрет на битие своей фигуры

def main():

    print()
    desk = show_desk(create_desk())
    while True:
        cage_1 = step('your figure position or exit: ')
        f_desk, steps = find_figure(desk, cage_1)
        print(f'permission steps: {steps}')
        cage_2 = step('your step or exit: ')
        update_desk(desk, player_step, (cage_1, cage_2))
        if cage_1 == 'exit' or cage_2 == 'exit': break


main()
