#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!


import sys

def replace_numbers(text):
    result = []
    for token in text.split():
        if token.isdigit():
            n = int(token)
            if n == 0:
                result.append(" ")          # 0 — пробел
            elif 1 <= n <= 26:
                result.append(chr(ord('a') + n - 1))  # 1→a, 2→b, ..., 26→z
            else:
                result.append(token)        # числа вне 0–26 не трогаем
        else:
            result.append(token)            # не числа не изменяем
    return "".join(result)


data = sys.stdin.read()
print(replace_numbers(data))