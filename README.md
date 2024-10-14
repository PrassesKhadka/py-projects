## Lessons Learnt

```
numbers = [1, 2, 3, 4, 5]
even_square_dict = {x: x**2 for x in numbers if x % 2 == 0}
Output: {2: 4, 4: 16}
```

- match-case in python -> equivalent of switch-case
- File Handling in Python:

```
 try:
   with open(fileName,'r'/'w'/'a') as file:
        file.write(data) or file.open()
 except Exception as e:
   print(f"{e}")
```

- List Comprehensions in Python

```
[expression for item in iterable if condition]

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_lists for item in sublist]
print(flattened)
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


<!-- left side is the operation on resultant value of i in iterated for-loop in right -->
<!-- [(expression/operation on item) for item in iterable if condition] -->

multiples = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(multiples)
Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)
Output: ['odd', 'even', 'odd', 'even', 'odd']


data = {"a": 1, "b": 2, "c": 3}
keys = [key for key in data]
print(keys)
Output: ['a', 'b', 'c']

```

- map(str or conversion function,iterables)
- sum(iterables)
- eval(string) convert string to dictionary
- strip() === trim() in js
- dictionary.items() or .values() or .keys() to iterate through dictionary
- [key,value for value in dictionary.items()]
- join and split functions
- "".join(map(str,students))
- if elif else
- random.randint(lower,higher)
