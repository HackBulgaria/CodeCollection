# counting substrings 

 Check how many times does a given substring occur in a given string. 

Implement a function, called ```count_substrings(haystack, needle)``` which returns the count of occurrences of the string ```needle``` in the string ```haystack```.

__Don't count overlapped substings and take case into consideration!__
For overlapping substrings, check the "baba" example below.

### Signature

```python
def count_substrings(haystack, needle):
    # Implementation
```

### Test examples

```
>>> count_substrings("This is a test string", "is")
2
>>> count_substrings("babababa", "baba")
2
>>> count_substrings("Python is an awesome language to program in!", "o")
4
>>> count_substrings("We have nothing in common!", "really?")
0
>>> count_substrings("This is this and that is this", "this")  # "This" != "this"
2
```