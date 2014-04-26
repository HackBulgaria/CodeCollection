# balanced numbers 

 Check if a given number is balanced 

A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number ```1238033``` is balanced, bacause it has a left part, equal to 123, and right part, equal ot 033.

We have : ```1 + 2 + 3 = 0 + 3 + 3 = 6```

A number with only one digit is always balanced.

Implement a function, called ```is_number_balanced(n)``` which checks if the given number is balanced.

### Signature

```python
def is_number_balanced(n):
    # Implementation
```

### Test examples

```
>>> is_number_balanced(9)
True
>>> is_number_balanced(11)
True
>>> is_number_balanced(13)
False
>>> is_number_balanced(121)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True
```