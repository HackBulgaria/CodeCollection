# calculate coins 

 Implement a function which returns the minimal amount of coins needed to represent a given sum 

This problem is from the [Python 2013 course in FMI](http://2013.fmi.py-bg.net/)

Implement a function, called ```calculate_coins(sum)``` where sum is a floating point number.

The function should return a dictionary, that represents a way to get the sum with minimal number of coins.

__The coins that we can use are with values 1,2,100,5,10,50,20.__

Check the examples below.

### Signature

```python
def calculate_coins(sum):
    # Implementation
```

### Test examples

```
>>> calculate_coins(0.53)
{1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0} # We pay with one coin of value 50 and two coins of value 2 and one coin of value 1 - that's the minimal number of coins to get to 0.53
>>> calculate_coins(8.94)
{1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}
```