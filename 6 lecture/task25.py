import random
import pickle

_dict = {'False': 'Логическое значение', 'None': 'Пустой', 'True': 'Истина', 'Python': 'Язык программирования'}

keys = list(_dict.keys())

class Game:
    def __init__(self):
        self.keys = keys
        self.ind = random.randint(0, len(self.keys) - 1)
        self.secret = self.keys[self.ind]
        self.mask = [' * '] * len(self.secret)
        self.guessed = set()

    def show_describe(self):
        """ Выводит описание слова """
        print(_dict[self.secret])

    def show_secret(self):
        """ Выводит слово """
        for val in self.mask:
            print(val, end="")
        print()

    def get_letter(self):
        letter = input("\n Введите букву:")
        return letter.strip()

    def check_letter(self, letter):
        letter = letter.upper()
        if not letter:
            return
        if letter in self.guessed:
            print("Буква уже угадывалась")
            return
        self.guessed.add(letter)

        hit = False
        for i, ch in enumerate(self.secret):
            if ch.upper() == letter.upper():
                self.mask[i] = f" {letter} "
                hit = True
        if not hit:
            print("Такой буквы нет!")

    def is_finished(self):
        return ' * ' not in self.mask

    # --- PICKLE ---
    def __getstate__(self):
        state = self.__dict__.copy()
        # set -> list для надёжности
        state['guessed'] = list(self.guessed)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.guessed = set(self.guessed)


def save_game(game, path='save_game.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(game, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"\nИгра сохранена в {path}")

def load_game(path='save_game.pkl'):
    with open(path, 'rb') as f:
        game = pickle.load(f)
    print(f"\nИгра загружена из {path}")
    return game


def start(game):
    while not game.is_finished():
        game.show_describe()
        game.show_secret()
        letter = game.get_letter()
        game.check_letter(letter)

        # автосохранение после хода
        save_game(game)

    print(f"\nПоздравляю! Слово: {game.secret}")


if __name__ == "__main__":
    try:
        game = load_game()
        print("Продолжаем сохранённую игру")
    except FileNotFoundError:
        game = Game()
        print("Новая игра")

    start(game)