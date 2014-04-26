# Sum of all digits 

 Find the sum of all digits between 1 and n 
 Given an integer, implement a function, called `sum_of_digits(n)` that calculates the sum of the digits of n.

 If a negative number is given, the function should work as if it was positive.

 For example, if n is `1325132435356`, the digit's sum is 43.
 If n is -10, the sum is 1 + 0 = 1

 Keep in mind that in Python, there is a special operator for integer division:

 ```
 >>> 5 / 2
 2.5
 >>> 5 // 2
 2
 ```

### Signature

```python
def sum_of_digits(n):
    # implementation
```

### Test examples

```
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```
