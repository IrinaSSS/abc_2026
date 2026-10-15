#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

cipher = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

def caesar_decrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

for shift in range(26):
    print(f"{shift:2}: {caesar_decrypt(cipher, shift)}")