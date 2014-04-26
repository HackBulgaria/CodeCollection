# contains digits 

 Check if a given number contains all of the digits in a given list. 

Implement a function, called ```contains_digits(number, digits)``` where ```digits``` is a __list of integers__ and a ```number``` is an integer.

The function should return True if __all__ ```digits``` are contained by ```number```

### Signature

```python
def contains_digits(number, digits):
    # Implementation
```

### Test examples

```
>>> contains_digits(402123, [0, 3, 4])
True
>>> contains_digits(666, [6,4])
False
>>> contains_digits(123456789, [1,2,3,0])
False
>>> contains_digits(456, [])
True
```