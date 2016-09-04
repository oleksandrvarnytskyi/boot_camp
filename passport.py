from data import Date


class OutOfSeries(Exception):
    pass


class InvalidNumber(Exception):
    pass


class InvalidSeries(Exception):
    pass


MAX_PASSPORT_NUMBER = 999999
FIRST_PASSPORT_SERIES = "AA"


class Passport:
    actual_series = FIRST_PASSPORT_SERIES
    actual_number = 1

    def __init__(self, name, last_name, birthday=Date()):
        self.name = name
        self.last_name = last_name
        Date.date_validation(birthday)
        self.birthday = birthday
        self.series = Passport.actual_series
        self.number = Passport.actual_number
        Passport.set_number()

    @staticmethod
    def set_number():
        Passport.actual_number += 1
        if Passport.actual_number > MAX_PASSPORT_NUMBER:
            if Passport.actual_series[1] == 'Z':
                if Passport.actual_series[0] == 'Z':
                    raise OutOfSeries
                Passport.actual_series = chr(ord(Passport.actual_series[0]) +
                                             1) + 'A'
                Passport.actual_number = 1
            else:
                Passport.actual_series = Passport.actual_series[0] + chr(ord(
                    Passport.actual_series[1]) + 1)
                Passport.actual_number = 1

    @staticmethod
    def valid_new_series(new_series):
        length = len(new_series)

        if length > 2:
            raise InvalidSeries()
        if not 'AA' <= new_series <= 'ZZ':
            raise InvalidSeries

    def set_new_series(self, new_series):
        self.valid_new_series(new_series)
        Passport.actual_series = new_series
        Passport.actual_number = 1

    def set_new_series_and_number(self, new_series, new_number):
        self.valid_new_series(new_series)

        if not 1 < new_number < MAX_PASSPORT_NUMBER:
            raise InvalidNumber()

        Passport.actual_series = new_series
        Passport.actual_number = new_number

    def __str__(self):
        return 'name: {0}\nlast name: {1}\nbirthday: {2}\n' \
               'passport series: {3}\npassport number: {4:06}\n'\
               .format(self.name, self.last_name, self.birthday,
                       self.series, self.number)


petro = Passport("Petro", "Pupkin", Date(14, 10, 1974))

petro.set_new_series("BA")

andrey = Passport("Andrey", "Goldfish", Date(1, 4, 1973))

print petro
print andrey
