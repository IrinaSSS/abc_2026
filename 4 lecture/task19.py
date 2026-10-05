#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm
import csv
from pathlib import Path
base_dir = Path(__file__).parent
file_path = base_dir / "algoritm.csv"
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
             "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
             "Наивный байесовский классификатор", "CART" ]
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    for i, name in enumerate(algoritm, start=1):
        file.write(f'{i}) "{name}"\n')        # каждый элемент в отдельной строке
# # Каждое значение из списка должно находится на отдельной строке.
# # Пример файла algoritm.csv:
# # 1) "C4.5"
# # 2) "k - means"
# # .....
# print(os.getcwd())