#!/usr/bin/env python2
# -*- coding: utf-8

from __future__ import print_function
from zeitansage import ZeitAnsage
import zahlwort

def main():
    print('\n------------------\n test Zahlwörter: \n------------------\n')
    print('normale Zahlen:')
    test_list = [
        -0, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, -15, 16, 17, 18, 19, 20,
        21, 30, 38, -42, 57, 63, 70, 75, 86, 94, 99, 100, 110, 350, 425, 515, 600,
        780, 803, 901, 1000, 1345, -2001, 3120, 4288, -5380, 6637, 7432, 8900, 9999,
        11000, -35902, 40679, 52960, 70000, 89200, -90255, 102034, 103572, 290356,
        305710, 460730, 589362, -612396, 710000, 891000, 902500
    ]
    for number in test_list:
        print('{:>7}: {}'.format(number, zahlwort.ZahlWort(number)))

    print('\nJahre:')
    test_list = [
        -0, -1, 2, 4, -15, 999, 1099, 1230, -1100, 1500, 1457, 1999, 2000, 2020
    ]
    for number in test_list:
        zahl = zahlwort.ZahlWort(number)
        print('{:>7}: {}'.format(number, zahl.jahrwort()))

    print('\nMonate:')
    test_list = [
        1, 2, 5, 12
    ]
    for number in test_list:
        zahl = zahlwort.ZahlWort(number)
        print('{:>7}: {}'.format(number, zahl.monatswort()))

    print('\nTage:')
    test_list = [
        1, 2, 5, 12, 15, 19, 20, 30, 31
    ]
    for number in test_list:
        zahl = zahlwort.ZahlWort(number)
        print('{:>7}: {}'.format(number, zahl.tagwort()))
    
    print('\n-------------------------\n test Datum und Uhrzeit: \n-------------------------\n')
    ansage = ZeitAnsage()
    list = (
        (1000, 1, 1, 0, 0), (-1243, 5, 2, 18, 0), (1999, 12, 31, 23, 59),
        (50, 8, 6, 12, 15), (2021, 2, 21, 16, 45), (-1845, 7, 31, 0, 0),
        (573824, 5, 8, 5, 14)
    )
    for time in list:
        ansage = ZeitAnsage()
        ansage.set_datetime(time)
        print('year: {}, month: {}, day: {}, {:02}:{:02}:\n-> {}'.\
            format(time[0], time[1], time[2], time[3], time[4], str(ansage)))

    print('\n\njetzt:')
    print(ZeitAnsage())

# def main():
#     ansage = zeitansage.zeitansage()
#     print('\nnumbers test:')
#     list = (
#         (0, 1, 2, 3), (4), (5, 6, 7), (8, 9), (10, 11, 12, 13, 14), (15, 16),
#         (17, 18, 19, 20), (22, 31, 46, 50, 57), (60, 63), (70, 78, 80, 84, 95),
#         (99, 100, 405, 824, 970), (1000), (1, 2, 3, 4, 5, 6)
#     )
#     for item in list:
#         ansage.getset_number(*item)
#         print(item, ansage.numwords())

#     print('\ntime test')
#     list = (
#         (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30), (12, 31), 
#         (12, 15), (12, 45), (11, 59), (23, 15), (23, 59), (12, 59), (13, 59),
#         (15, 22), (1, 60), (24, 00)
#     )
#     for item in list:
#         ansage.set_time(*item)
#         print(ansage.digits(), ansage.colloquial())

#     ansage.set_time() #set time to now
#     print('\nlocal time is ' + ansage.colloquial())
        

if __name__ == "__main__": main()
