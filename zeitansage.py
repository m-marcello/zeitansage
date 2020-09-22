#!/usr/bin/env python2

from zahlwort import ZahlWort
from datetime import datetime

class ZeitAnsage(object):
    def __init__(self):
        now = datetime.now()
        self._year = ZahlWort(now.year)
        self._month = ZahlWort(now.month)
        self._day = ZahlWort(now.day)
        self._hour = now.hour
        self._minute = now.minute

    def __str__(self):
        ansagetext = self.datumsansage() + ', ' + self.uhrzeitansage()
        return ansagetext 

    def set_date(self, (year, month, day)):
        self._year = ZahlWort(year)
        if month < 1 or 12 < month:
            raise IndexError('month of {} is out of bound'.format(month))
        self._month = ZahlWort(month)
        if day < 1 or 31 < day:
            raise IndexError('day of {} is out of bound'.format(day))
        if (day == 31 and month in (4, 6, 9, 11)) or (day > 28 and month == 2):
            raise TypeError('date: {}.{} does not exist'.format(month, day))
        self._day = ZahlWort(day)

    def set_time(self, (hour, minute)):
        if (hour < 0 or 23 < hour) or (minute < 0 or 59 < minute):
            raise IndexError('time {}:{} does not exist'.format(hour, minute))
        self._hour = hour
        self._minute = minute

    def set_datetime(self, (year, month, day, hour, minute)):
        self.set_date((year, month, day))
        self.set_time((hour, minute))

    def update_datetime(self):
        now = datetime.now()
        self.set_date(now.jear, now.month, now.day)
        self.set_time(now.hour, now.minute)

    def datumsansage(self):
        return (self._day.tagwort() + ' ' + self._month.monatswort() + \
            ' des Jahres ' + self._year.jahrwort())
    
    def uhrzeitansage(self):
        hour = self._hour
        minute = self._minute
        prepositon = ' '
        if minute >= 30:
            hour = hour + 1
        if minute < 30:
            prepositon = ' nach '
        if minute > 30:
            prepositon = ' vor '
            minute = 60 - minute
        if hour % 12 > 0:
            hour = hour % 12
        minutenansage = ZahlWort(minute).zahlwort()
        stundenansage = ZahlWort(hour).zahlwort()
        if hour == 0 or hour == 24:
            stundenansage = 'Mitternacht'
        if minute == 15 or minute == 45:
            minutenansage = 'viertel'
        if minute == 30:
            minutenansage = 'halb'
        if minute == 0:
            minutenansage = ''
            prepositon = ''
            if hour != 0:
                stundenansage = stundenansage + ' Uhr'
        return (minutenansage + prepositon + stundenansage)


def main():
    print(ZeitAnsage())

if __name__ == "__main__": main()
