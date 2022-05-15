from new1 import *

d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
h = [1, 2, 3, 4, 5, 6, 7, 8]
fig = ['rook','knight','bishop','king','queen','bishop','knight','rook']

b_w = ['black', 'white']
player_step = b_w[1]
memory_w_b = [[], []]
# figure_w_b = {'king': ({'white': 9818, 'black': 9812}, lambda: king),
#             'queen': (9819, 9813, lambda: queen),
#             'bishop': (9821, 9815, lambda: bishop),
#             'knight': (9822, 9816, lambda: knight),
#             'rook': (9820, 9814, lambda: rook),
#             'pawns': (9823, 9817, lambda: pawns)}

# def create_desk(s, rowFig, rowPawns, color = 0):
#
#     for i in range(0, len(d)):
#         s[d[i]+str(rowFig)] = s.get(d[i]+str(rowFig))[0], fig[i], chr(figure_w_b[fig[i]][color]), b_w[color]
#
#     a = [i + str(rowPawns) for i in d]
#
#     for i in a:
#         s[i] = s.get(i)[0], 'pawns',  chr(figure_w_b['pawns'][color]), b_w[color]
#
#     return s


# def blank_desk():
#
#     s = {}
#     for i in d:
#         for v in h:
#             pass
#             s[i + str(v)] = (d.index(i) , h.index(v)), None, '  ', None
#     return s
# s = {'a1': (1,2,lambda :show)}

# def show(a,b):
#     print(f'a {a}')
#     print(f'b {b}')

# c = s.get('a1')[2]
# a = s.get('a1')[2]()
s.get('a1')[2]()('hello', 'world')
# print(c)
# print(a)
# print(b)

