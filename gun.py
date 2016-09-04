class NotReady(Exception):
    pass


class OutOfRounds(Exception):
    pass


class Gun:
    def __init__(self, model, capacity, amount=0, total_shots=0,
                 is_ready=False):
        self.model = model
        self.capacity = capacity
        self.amount = amount
        self.total_shots = total_shots
        self.is_ready = is_ready

    def prepare(self):
        self.is_ready = not self.is_ready

    def reload(self):
        self.amount = self.capacity

    def shot(self):
        if not self.is_ready:
            raise NotReady()
        if self.amount == 0:
            raise OutOfRounds()

        self.total_shots += 1
        self.amount -= 1
        print "Bang!\n"

        if self.amount == 0:
            self.is_ready = False
            print "Please reload your weapon!"

    def __str__(self):
        return 'Model: {0}\ncapacity: {1}\namount: {2}\ntotalShots: {3}\n' \
               'readiness: {4}\n'.format(self.model, self.capacity,
                                         self.amount, self.total_shots,
                                         self.is_ready)


beretta = Gun('Beretta', 10)
colt = Gun('Colt', 8)

print beretta
print colt
beretta.reload()
beretta.prepare()
beretta.shot()
print beretta
beretta.amount = 0

try:
    beretta.shot()
except OutOfRounds:
    print "out of rounds exception was called!"
