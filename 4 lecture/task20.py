#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().
import csv
from pathlib import Path
base_dir = Path(__file__).parent
file_path = base_dir / "inverted_sort.txt"

data = ["Beautiful is better than ugly.", "Explicit is better than implicit." ,
       "Simple is better than complex.", "Complex is better than complicated." ]

with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow([row])   

with open(file_path, 'r', encoding='utf-8-sig') as file:
    lines = file.readlines()

clean_line = []
for line in lines:
    clean_line.append(line.strip())  # убираем \n и пробелы по краям

with open(file_path, 'a', encoding='utf-8-sig') as file:
    file.write('\n')
    for line in clean_line[::-1]:
        file.write(line + '\n')


# #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.