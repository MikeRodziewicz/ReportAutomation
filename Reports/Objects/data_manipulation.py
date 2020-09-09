from datetime import date, timedelta


class Date_Stamps():

    the_date = None

    def __init__(self):
        self.time = date.today()

    def get_today(self):
        return self.time

    def get_yesteday(self):
        the_date = self.time - timedelta(days=1)
        return the_date

    def count_in_weekend(self):
        if self.time.isoweekday() == 1:
            the_date = self.time - timedelta(days=3)
            return the_date
        else:
            return self.get_yesteday()

    def get_start_month(self):
        the_date = self.time.replace(day=1)
        return the_date

    def __str__(self):
        return f'today is {self.time}'

