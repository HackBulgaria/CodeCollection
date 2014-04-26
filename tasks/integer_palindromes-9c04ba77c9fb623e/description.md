# Integer palindromes 

 Check if a given integer is a palindrome. 

A palindrome is а word or a phrase or a number, that when reversed, stays the same.

For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".

But this time, we are not interested in words but numbers.
A number palindrome is a number, that taken backwards, remains the same.

For example, the numbers 1, 4224, 9999, 1221 are number palindromes.

Implement a function, called ```is_int_palindrome(n)``` which takes an integer and returns True, if this integer is a palindrome.

### Signature

```python
def is_int_palindrome(n):
    # implementation
```

### Test examples

```
>>> is_int_palindrome(1)
True
>>> is_int_palindrome(42)
False
>>> is_int_palindrome(100001)
True
>>> is_int_palindrome(999)
True
>>> is_int_palindrome(123)
False
```