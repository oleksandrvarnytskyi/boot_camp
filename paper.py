class Paper:
    def __init__(self, max_symbols=100):
        self.max_symbols = max_symbols
        self.symbols = 0
        self.content = ''

    def add_content(self, message):
        self.symbols += len(message)
        self.content += message

    def show(self):
        print self.content


if __name__ == '__main__':
    paper = Paper(10)
    paper.add_content("Hello Python!")
    paper.show()
