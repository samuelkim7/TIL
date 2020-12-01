### map() function
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
