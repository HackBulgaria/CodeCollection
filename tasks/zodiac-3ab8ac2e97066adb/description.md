# zodiac 

 Make a function that returns the zodiac sign for a given date. 

This problem is from the Python 2013 course in FMI. [Link to original problem statement.](http://2013.fmi.py-bg.net/tasks/1)

Implement a function, called ```what_is_my_sign(day, month)``` which takes two integers (one for the day and one for the month) and returns the name of the zodiac for the given time period.

Consider the following zodiac table ([Or check wikipedia](http://en.wikipedia.org/wiki/Zodiac#Table_of_dates)) :

* Aries: 21 March – 20 April
* Taurus: 21 April – 21 May
* Gemini: 22 May – 21 June
* Cancer: 22 June – 22 July
* Leo: 23 July – 22 August
* Virgo: 23 August – 23 September
* Libra: 24 September – 23 October
* Scorpio: 24 October – 22 November
* Sagittarius: 23 November – 21 December
* Capricorn: 22 December – 20 January
* Aquarius: 21 January – 19 February
* Pisces: 20 February – 20 March


### Signature

```python
def what_is_my_sign(day, month):
    # Implementation
```

### Test examples

```
>>> what_is_my_sign(5, 8)
"Leo"
>>> what_is_my_sign(29, 1)
"Aquarius"
>>> what_is_my_sign(30, 6)
"Cancer"
>>> what_is_my_sign(31, 5)
"Gemini"
>>> what_is_my_sign(2, 2)
"Aquarius"
>>> what_is_my_sign(8, 5)
"Taurus"
>>> what_is_my_sign(9, 1)
"Capricorn"
```
