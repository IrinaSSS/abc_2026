# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

# Задачу решить без функций max и прочих.
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
mass = [x, y, z]
for k in range(0, len(mass) - 1):
    for i in range(0,len(mass) - 1 -k ):
        if mass[i] > mass[i+1]:
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
print("max = ", mass[-1])