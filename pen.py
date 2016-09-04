from paper import Paper


class OutOfInk(Exception):
    pass


class OutOfSpace(Exception):
    pass


class Pen:
    def __init__(self, ink_capacity):
        self.ink_capacity = ink_capacity
        self.ink_amount = ink_capacity

    def refill(self):
        self.ink_amount = self.ink_capacity

    def write(self, message, paper):
        message_size = len(message)
        empty_space = paper.max_symbols - paper.symbols
        counter_of_spaces = 0

        if self.ink_amount == 0:
            raise OutOfInk()
        if empty_space == 0:
            raise OutOfSpace()
        if message_size > empty_space:
            new_message = message[:empty_space]
            message_size = len(new_message)
        else:
            new_message = message

        space = new_message.find(' ')
        ink_needed = space

        while space != -1 and ink_needed < self.ink_amount and space < \
                empty_space:
            counter_of_spaces += 1
            ink_needed -= counter_of_spaces
            space = new_message.find(' ', space+1)

        if message_size > self.ink_amount:
            new_message = new_message[:self.ink_amount+counter_of_spaces]
            self.ink_amount = 0
            paper.add_content(new_message)
        else:
            self.ink_amount -= message_size - counter_of_spaces
            paper.add_content(new_message)


pen = Pen(10)
paper = Paper(35)

pen.write("      Hello,  world!", paper)
paper.show()
# pen.write(" Hello, python!", paper)
paper.show()


