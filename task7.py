#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a = int(input("введите А:"))
b = int(input("введите B"))
c = int(input("введите C:"))


points = [
    ("A", a),
    ("B", b),
    ("C", c),
]

d = {name: coord for name, coord in points}
print("длина отрезка АС: ", abs(d["A"] - d["C"]))
print("длина отрезка BC: ", abs(d["B"] - d["C"]))
print("cумма длинн отрезков АС и ВС:", abs(d["A"] - d["C"]) + abs(d["B"] - d["C"]))