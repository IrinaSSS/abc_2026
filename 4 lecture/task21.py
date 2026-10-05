#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
import csv
from pathlib import Path
base_dir = Path(__file__).parent
file_path = base_dir / "config_default.txt"

data = ["app_name    = ?", "version     = ?" ,
       "debug       = ?", "# Настройки базы данных", "db_host     = ?", "db_port     = ?", 
       "db_name     = ?", "db_user     = ?", "db_password = ?",
       "# Настройки API", "api_key     = ?", "api_secret  = ?", "base_url    = ?",
       "# Пути", "log_file    = ?", "data_dir    = ?", "temp_dir    = ?"]

with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
    file.write('\n'.join(data)) 

# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

with open(file_path, 'r', encoding='utf-8-sig') as file:
    lines = file.readlines()
new_lines = []
for line in lines:
    stripped = line.lstrip()
    # комментарии и пустые строки оставляем как есть
    if stripped.startswith('#') or not stripped.strip():
        new_lines.append(line)
        continue

    if '?' in line:
        # ключ это всё до первого =
        key = line.split('=', 1)[0].strip()
        if key in config_values:
            value = str(config_values[key])
            # заменяем только первое вхождение ?
            line = line.replace('?', value, 1)
    new_lines.append(line)

# если нужно сохранить
with open(file_path, 'w', encoding='utf-8-sig') as f:
    f.writelines(new_lines)


# print(type(config_values))
# keys_dict = list(config_values.keys())
# with open(file_path, 'r', encoding='utf-8-sig') as file:
#     lines = file.readlines()

# print(lines)
# clean_line = []
# for line in lines:
#     if line[0] == "#":
#         continue
#     else:
#         clean_line.append(line.split()[0])

# print(clean_line)

# idx = [keys_dict.index(val) for val in clean_line if val in config_values]
# print(idx)

# new_config = [line.replace("?", config_values[keys_dict[i]]) for i in idx]


# print(new_config)
# with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
#     f.writelines(line)

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True

# # Настройки базы данных
# db_host     =  5432
# .....