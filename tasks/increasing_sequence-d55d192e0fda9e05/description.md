# increasing sequence 

 Check if a given sequence is monotonously increasing. 

Implement a function, called ```is_increasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously increasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously increasing if for every two elements a and b, that are next to each other (a is before b), we have a < b

For example, ```[1,2,3,4,5]``` is monotonously increasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_increasing(seq):
    # Implementation
```

### Test examples

```
>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False
```