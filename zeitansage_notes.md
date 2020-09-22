# zeitansage

## what I need:

in zahlwort:
- `__str__(self)`: creates the string for the number in the object
- `getset_num(self, num=None)`: returns the number in the object (if num is given, number is overridden first)
- `zahlwort(self, num=None)`: return the German word for the object or the given num
- `jahrwort(self, num=None)`: returns the word for the year
- `monatswort(self, num=None)`: returns the word for the month
- `tagwort(self, num=None)`: returns the word for the day

in zeitansage:
- `__str__(self)`: the current date and time in German colloquial
- `zeit()` returns the ansage object (year, month, day, hour, minute)
- `set_numbers(self, numbers)`: numbers is a single number or a tuple of numbers<br>
len(numbers) <= 5, sets the self as those numbers with None when no number is given
- `numword_preposition(self)`: return the preposition to be used in the time (13:24 -> nach, 13:40 -> vor, 13:30 -> None)
- `numword_num(self)`: returns the word for the number
- `set_time(self, time)`: overrides the hour and minute of zeitansage object with the given tuple time
- `set_date(self, date)`: overrides the year, month and day of zeitansage object with the given tuple date
- `get_now(self)`: fills ansage object with the date and time of right now