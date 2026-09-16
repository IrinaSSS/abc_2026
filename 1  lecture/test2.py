# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку
age = "23"
foo = "23abc" # не перевести в класс int целиком
age_int = int(age)
foo_num = ""
for i in foo:
    if i.isdigit():
        foo_num += i
    else:
        break
foo_int = int(foo_num)
print(type(age_int), type(foo_int))
age = "123abc"
print(type(bool(foo)))
flag = 1
print(type(bool(flag)))
str_one = "Privet"
str_two = ""
print(type(bool(flag)), type(bool("str_one")))
print(type(bool(1)), type(bool(0)))
print(type(str(False)))