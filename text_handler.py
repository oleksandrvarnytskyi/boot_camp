class TextHandler:
    def __init__(self, filename):
        self.filename = filename
        self.characters = set()
        self.characters_statistics = {}
        self.numbers = set()
        self.numbers_statistics = {}
        self.special_symbols = set()
        self.special_symbols_statistics = {}
        self.words = set()
        self.words_statistics = {}
        self.quantity = 0

    @staticmethod
    def insert_statistic(dictionary, symbols):
        if symbols in dictionary:
            value = dictionary.get(symbols)
            dictionary.update({symbols: value+1})
        else:
            value = 1
            dictionary.update({symbols: value})

    @staticmethod
    def get_from_set(in_set):
        return list(in_set)

    @staticmethod
    def get_from_dic(in_dic):
        return '\n'.join(key + ' = ' + str(in_dic[key]) + ' matches' for key
                         in in_dic)

    def parse_text(self):
        in_file = open(self.filename)
        word = ''
        number = ''

        for symbol in iter(lambda: in_file.read(1), ''):
            if symbol == ' ':
                if word:
                    self.words.add(word)
                    self.insert_statistic(self.words_statistics, word)
                    word = ''
                if number:
                    self.numbers.add(number)
                    self.insert_statistic(self.numbers_statistics, number)
                    number = ''
                self.quantity += 1

            if symbol.isalpha():
                if symbol.isupper():
                    symbol = symbol.lower()
                self.characters.add(symbol)
                self.insert_statistic(self.characters_statistics, symbol)
                self.quantity += 1
                word += symbol

            if symbol.isdigit():
                number += symbol
                self.quantity += 1
                if word:
                    self.words.add(word)
                    self.insert_statistic(self.words_statistics, word)
                    word = ''

            if not symbol.isalnum():
                self.special_symbols.add(symbol)
                self.insert_statistic(self.special_symbols_statistics, symbol)
                self.quantity += 1
                if word:
                    self.words.add(word)
                    self.insert_statistic(self.words_statistics, word)
                    word = ''
                if number:
                    self.numbers.add(number)
                    self.insert_statistic(self.numbers_statistics, number)
                    number = ''
        in_file.close()

    def __repr__(self):
        return '\nSymbols found: {0}\n\nLetters statistic:\nUnique:\n{1}\n' \
               'Matches in text:\n{2}\n\nNumbers statistic:\n' \
               'Unique:\n{3}\nMatches in text:\n{4}\n\nSpecial symbols ' \
               'statistic:\nUnique:\n{5}\nMatches in text:\n{6}\n\nWords ' \
               'statistic:\nUnique:\n{7}\nMatches in text: \n{8}\n'.format(
                self.quantity, TextHandler.get_from_set(self.characters),
                TextHandler.get_from_dic(self.characters_statistics),
                TextHandler.get_from_set(self.numbers),
                TextHandler.get_from_dic(self.numbers_statistics),
                TextHandler.get_from_set(self.special_symbols),
                TextHandler.get_from_dic(self.special_symbols_statistics),
                TextHandler.get_from_set(self.words),
                TextHandler.get_from_dic(self.words_statistics))


handler = TextHandler('symbols.txt')
handler.parse_text()
print handler
