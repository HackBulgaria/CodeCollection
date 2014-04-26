# n sevens in a row 

 Check if a given array contains n consecutive sevens 

Implement a function, called ```sevens_in_a_row(arr, n)```, which takes an array of integers ```arr``` and a number ```n > 0```

The function returns True, __if there are n consecutive sevens__ in ```arr```

For example, if ```arr``` is ```[10, 8, 7, 6, 7, 7, 7, 20, -7]``` and n is 3, the function should return True. Otherwise, it returns False

### Signature

```python
def sevens_in_a_row(arr, n)
```

### Test examples

```
>>> sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
True
>>> sevens_in_a_row([1,7,1,7,7], 4)
False
>>> sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
True
>>> sevens_in_a_row([7,2,1,6,2], 1)
True
```