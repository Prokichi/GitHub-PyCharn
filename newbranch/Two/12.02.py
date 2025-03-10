def insert_asterisks(matr, L, R):
    n = len(matr)
    for i in range(n):
        for j in range(n):
            if eval(L) <= j <= eval(R):
                matr[i][j] = '*'


_1 = 'i'
_2 = 'n-i-1'


def U(matr):
    insert_asterisks(matr, _1, _2)

def D(matr):
    insert_asterisks(matr, _2, _1)

def L(matr):
    insert_asterisks(matr, '0', f'min({_1}, {_2})')

def R(matr):
    insert_asterisks(matr, f'max({_1}, {_2})', 'n-1')

def go():
    figure = {
        1: ['А', [U, R]],
        2: ['Б', [L, D]],
        3: ['В', [U]],
        4: ['Г', [D]],
        5: ['Д', [U, D]],
        6: ['Е', [L, R]],
        7: ['Ж', [L]],
        8: ['З', [R]],
        9: ['И', [U, L]],
        10: ['К', [R, D]]
    }

    def input_fig_num():
        while True:
            print()
            for k, v in figure.items():
                print(f'{k}. {v[0]}')
            num = int(input('\nВыберите номер фигуры: '))
            if num in figure:
                return num

    while True:
        num = input_fig_num()
        size = int(input('Введите длину стороны квадрата: '))
        if size % 2 == 0:
            size -= 1
        matr = [[' '] * size for _ in range(size)]
        for fun in figure[num][1]:
            fun(matr)
        print(f'\n{num}.{figure[num][0].upper()}:')
        for row in matr:
            print(*row)
        if input('Выйти из программы(1)?: ') == '1':
            break

go()
