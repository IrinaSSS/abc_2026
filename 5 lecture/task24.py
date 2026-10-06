# todo: Шифр Цезаря
Описание шифра.
В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
является одним из самых простых и широко известных методов шифрования.
Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

Задача.
Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

from pathlib import Path

with open("message.txt", "w", encoding="utf-8") as f:
    f.write("питон\n")


# Алфавит кириллицы, 33 буквы
LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
UPPER = LOWER.upper()
ALPHABET = {ch:i for i,ch in enumerate(LOWER)}
ALPHABET.update({ch:i for i,ch in enumerate(UPPER)})

def caesar_cyrillic(text: str, shift: int) -> str:
    res = []
    for ch in text:
        if ch in ALPHABET:
            # сдвиг влево = минус shift
            base = UPPER if ch.isupper() else LOWER
            idx = ALPHABET[ch]
            new_idx = (idx - shift) % len(LOWER)
            res.append(base[new_idx])
        else:
            res.append(ch)
    return ''.join(res)

path = Path('message.txt')
if not path.exists():
    raise FileNotFoundError('Файл message.txt не найден')

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

encrypted_lines = []
for i, line in enumerate(lines, start=1):
    shift = i  # 1-я строка -1, 2-я -2 и т.д.
    enc_line = caesar_cyrillic(line.rstrip('\n'), shift)
    encrypted_lines.append(enc_line + '\n')

# Вывод в консоль
for l in encrypted_lines:
    print(l, end='')

# Сохранить в файл
Path('message_encrypted.txt').write_text(''.join(encrypted_lines), encoding='utf-8')

