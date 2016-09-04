class InvalidDate(Exception):
    pass


class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year
        Date.date_validation(self)

    def date_validation(self):
        month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        real_month = self.month - 1

        if self.year % 4 == 0 and (self.year % 100 != 0 or
                                   self.year % 400 == 0):
            month_lengths[1] = 29
        if not 0 < self.month < 13:
            print "here"
            raise InvalidDate()
        if not 0 < self.day <= month_lengths[real_month]:
            print "here2"
            raise InvalidDate()

    def __str__(self):
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                       "Sep", "Oct", "Nov", "Dec"]
        return '%s %s %s %s' % (self.day, month_names[self.month-1], self.year,
                                ('BC' if self.year < 0 else 'AD'))


if __name__ == '__main__':
    try:
        date = Date()
        print date
    except InvalidDate:
        print 'Invalid date!'
