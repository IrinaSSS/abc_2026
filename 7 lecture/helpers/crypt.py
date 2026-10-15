def caesar_cipher(text, shift=3, decrypt=False):
    """
    Шифр Цезаря для латиницы и кириллицы.
    decrypt=True — расшифровка (сдвиг в обратную сторону).
    Регистр и не-буквенные символы сохраняются.
    """
    if decrypt:
        shift = -shift

    def shift_alpha(alpha, ch, shift):
        if ch in alpha:
            return alpha[(alpha.index(ch) + shift) % len(alpha)]
        return ch

    lower_en = "abcdefghijklmnopqrstuvwxyz"
    upper_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    upper_ru = lower_ru.upper()

    result = []
    for ch in text:
        for alpha in (lower_en, upper_en, lower_ru, upper_ru):
            new_ch = shift_alpha(alpha, ch, shift)
            if new_ch != ch:
                result.append(new_ch)
                break
        else:
            result.append(ch)
    return "".join(result)