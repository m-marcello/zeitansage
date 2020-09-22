#!/usr/bin/env python2
# -*- coding: utf-8

from __future__ import print_function
import os, sys

class ZahlWort(object):
    """
    generates a string how a German would say a number
    within, not including -1,000,000 and +1,000,000
    """
    pow0 = (
        None, 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben',
        'acht', 'neun'
    )
    special_pow0 = (
        None, 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben',
        'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn',
        'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn'
    )
    pow1 = (
       None, None, 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig',
       'siebzig', 'achtzig', 'neunzig'
    )
    pow2 = 'hundert'
    pow3 = 'tausend'

    def __init__(self, num=0):
        self._num = num

    def __str__(self):
        num = self.getset_num()
        numword = ''
        if num == 0:
            return 'null'
        elif abs(num) >= 1000000:
            return 'OOR'
        if num < 0:
            numword = 'minus '
            num = abs(num)
        if num > 999:
            if num > 1999:
                numword = numword + self.zahlwort(int(num / 1000)) + 'tausend'
            else:
                numword = numword + 'eintausend'
            num = int(num % 1000)
        if num == 0: return numword
        if num > 99:
            numword = numword + self.pow0[int(num / 100)] + 'hundert'
            num = int(num % 100)
        if num == 0: return numword
        if 100 > num >= 20:
            if int(num % 10) != 0:
                numword = numword + self.pow0[int(num % 10)] + 'und' + \
                    self.pow1[int(num / 10)]
            elif int(num % 10) == 0:
                numword = numword + self.pow1[int(num / 10)]
        elif num < 20:
            numword = numword + self.special_pow0[num]
        return numword

    def getset_num(self, num=None):
        if num:
            self._num = num
        return (self._num)

    def zahlwort(self, num=None):
        num = self.getset_num(num)
        return str(ZahlWort(num))
    
    def jahrwort(self, num=None):
        num = self.getset_num(num)
        yearword = ''
        suffix = ''
        if num < 0:
            suffix = ' vor Christi'
            num = abs(num)
        if 1100 <= num < 2000:
            yearword = self.zahlwort(int(num / 100)) + 'hundert'
            num = int(num % 100)
            if num != 0:
                yearword = yearword + self.zahlwort(int(num % 100))
        else:
            yearword = self.zahlwort(num)
        return yearword + suffix

    def monatswort(self, num=None):
        monate = (
            None, 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli',
            'August', 'September', 'Oktober', 'November', 'Dezember'
        )
        num = self.getset_num(num)
        if num < 1 or 12 < num:
            raise IndexError('month out of bound: received month {}'.format(num))
        return monate[num]

    def tagwort(self, num=None):
        exceptions = {1: 'erster', 3: 'dritter', 8: 'achter'}
        num = self.getset_num(num)
        if num < 1 or 31 < num:
            raise IndexError('days out of bound: received day {}'.format(num))
        if num in exceptions:
            return exceptions[num]
        if num < 20:
            return self.zahlwort(num) + 'ter'
        else:
            return self.zahlwort(num) + 'ster'
