# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

print("Введите тип сортировки: ")
print("1. По возрасту")
print("2. По первой букве")
print("3. По группе")

choice = int(input("Тип сортировки: "))

if choice == 1:
    age = int(input("Введите критерии поиска: "))
    result = [u for u in users if u['age'] > age]

elif choice == 2:
    letter = input("Введите критерии поиска: ").strip()
    result = [u for u in users if u['login'][0].lower() == letter.lower()]
    
elif choice == 3:
    group = input("Введите критерии поиска: ").strip()
    result = [u for u in users if u['group'] == group]

else:
    print("Неверный тип сортировки")
    result = []

if result == []: print("совпадений не найдено")
else:
    print("\nРезультат:")
    for u in result:
        print(f"Пользователь: '{u['login']}' возраст {u['age']} года , группа  \"{u['group']}\"")



