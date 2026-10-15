#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36


# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

data = [
    [11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [31, 32, 33, 34, 35, 36],
]

with open('matrix.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(' '.join(map(str, row)) for row in data))

def load_matrix(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # читаем только непустые строки
            lines = [line.strip() for line in f if line.strip() != '']
    except Exception:
        return False

    # преобразуем каждую строку в список int с помощью list comprehension
    rows = [list(map(int, line.split())) for line in lines]

    if not rows:
        return False

    # длины всех строк должны совпадать
    lens = [len(r) for r in rows]
    return rows if len(set(lens)) == 1 else False

if __name__ == "__main__":
    mat = load_matrix('matrix.txt')
    print(mat)