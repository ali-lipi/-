# ЗАДАЧА 1 (4 минуты).

def lst(array_):
    return ", ".join(array_) + '.'


city = ['Москва', 'Санкт-Петербург', 'Воронеж']
print(lst(city))
print()


# ЗАДАЧА 2 (42 минуты).

def number(num):
    tail = round(num % 10, 1)

    if 0 <= tail < 2.5:
        return num - tail
    elif 2.5 <= tail < 7.5:
        return num - tail + 5
    elif 7.5 <= tail < 10:
        return num - tail + 10


print(f'для {27}:', number(27))
print(f'для {27.8}:', number(27.8))
print(f'для {41.7}:', number(41.7))
print(f'для {37.4}:', number(37.4))
print(f'для {50}:', number(50))
print()


# ЗАДАЧА 3 (8 минут).

def computer(num):
    dic = {
        1: "компьютер",
        2: "компьютера",
        3: "компьютера",
        4: "компьютера",
        5: "компьютеров",
        6: "компьютеров",
        7: "компьютеров",
        8: "компьютеров",
        9: "компьютеров",
        0: "компьютеров",
    }

    return str(num) + ' ' + dic[num % 10]


print(computer(25))
print(computer(41))
print(computer(1048))
print(computer(4))
print()


# ЗАДАЧА 4 (4 минуты).

def number(num):
    i = 2
    while num % i != 0 and i < num:
        i += 1
    return f'Число {num} является простым' if i == num else f'Число {num} не является простым'


print(number(9))
print(number(5))
print()


# ЗАДАЧА 5. (6 минут. Сначала начала решать через множества и их обьединение, потом учла условие >=2.)

def intersection(a, b):
    my_list = a + b
    return [i for i in range(len(my_list)) if my_list.count(i) >= 2]


# данные из примера    
array1 = [7, 17, 1, 9, 1, 17, 56, 56, 23]
array2 = [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]

print(intersection(array1, array2))
print()


# ЗАДАЧА 6 (31 минута).

def matrix(n):
    n_new = n + 1  # учла доп. столбец
    mtrx = [[0] * n_new for i in range(0, n_new + 1)]

    for i in range(n_new):
        for j in range(n_new):
            if j == 0 and i != 0:
                mtrx[i][j] = i
            if i == 0 and j != 0:
                mtrx[i][j] = j
            if i != 0 and j != 0:
                mtrx[i][j] = i * j

    mtrx[0][0] = ' '

    for i in range(n_new):
        for j in range(n_new):
            # if нужен, чтобы убрать лишний пробел между нулевым и первым столбцом (согласно условию задачи)
            if (j == 0 and n < 10) or (j == 1 and n < 10):
                print(str(mtrx[i][j]).rjust(2), end='')
            else:
                print(str(mtrx[i][j]).rjust(3), end='')
        print()


matrix(5)
print()
matrix(9)
print()
