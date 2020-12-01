### basics
#### map() function
- map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
- Syntax: map(fun, iter)
  
Ex)
```python
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result))
```
Output:
```python
[2, 4, 6, 8]
```

#### print() function
- parameters: sep, end 

#### == and is
==(equals) : comparing the values of the two variables 
is : checking if the two variables point to the same object

### Sequence types
- sequence is the generic term for an ordered set. List, tuple, range, str, bytes, bytearray are sequence types.
- Lists are the most versatile sequence type. The elements of a list can be any object, and lists are mutable they can be changed. Elements can be reassigned or removed, and new elements can be inserted.
- Tuples are like lists, but they are **immutable - they can't be changed.**
- Strings are a special type of sequence that can only store characters, and they have a special notation. However, all of the sequence operations described below can also be used on strings. Strings are **immutable.**
- sequence operations: +, \*, [i], slicing (+ and \* cannot be applied on range object)
- functions for sequence: len(), min(), max(), seq.index(x), seq.count(x)
- tuples and strings and ranges are immutable. So reassigning values cannot be done on them.
