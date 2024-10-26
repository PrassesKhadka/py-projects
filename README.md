## Lessons Learnt

- strings in Python are immutable
- label.replace() method returns a new string, but doesn't modify the original string in place

- Async Context Manager in Python -> To manage resources asynchronously
  such as connecting to databases,opening files, or acquiring locks

```
from contextlib import asynccontextmanager

@asynccontextmanager -> Converts the function into something called and "async context manager"

- A context manager in Python is something that you can use in a `with` statement. For Example open() can be used as a context manager

with open("file.txt) as f:
    // code

async with lifespan(app):
    await do_stuff()

When you create a context manager or an async context manager like above, what it does is that, before entering the with block, it will execute the code before the yield, and after exiting the with block, it will execute the code after the yield.
```

Example code:

```
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource_manager():
    # Asynchronous setup code
    print("Acquiring resource")
    await asyncio.sleep(1)  # Simulate an async operation, e.g., connecting to a database
    resource = "my_resource"  # Replace with actual resource
    try:
        # The yield statement allows the function to temporarily return the
        # resource to the caller (the block of code that uses the context
        # manager). The code execution will pause here until the block completes.
        # Yield: The yield statement provides the resource to the block of code inside the async with statement.
        # After yield: cleanup code.

        yield resource  # This is where the resource is made available
    finally:
        # Asynchronous teardown code
        print("Releasing resource")
        await asyncio.sleep(1)  # Simulate an async operation, e.g., closing the database connection

async def main():
    <!-- resource from yield in async_resource_manager received here -->
    async with async_resource_manager() as resource:
        print(f"Using resource: {resource}")
        <!-- after this gets complete, finally in async_resource_manager() gets executed -->
        await asyncio.sleep(1)  # Simulate work with the resource

# Run the main function
asyncio.run(main())

```

- Slice Notations in Python:

```
sequence[start:end:step]

Eg:
files = [filename[:-4] for filename in os.listdir(DATA_PATH) if filename.endswith(".txt")]
filename[:-4]-> Returns filename discarding .txt

Eg:
item = "hello"
print(item[1:]) # Output: "ello"

item = "hello"
print(item[::2])  # Output: "hlo"
```

- all(iterable) -> Returns True or False -> equivalent to array.every(callback) in js

```
print(all(["hello", "world", ""]))  # Output: False (because of the empty string)

numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # Output: True (all numbers are even)
```

- Dict Comprehensions

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

<!-- Returns list of lines -->

- f.readlines()
- f.write(f"{str(label)}\n")
<!-- Returns list of directory/files names inside the path RAW_DIR  -->
- os.listdir(RAW_DIR)
- os.path.join(RAW_DIR,"animals")
- os.path.exists(img_path)
- <!-- Returns list of files matching the path -->

  ```
  glob.glob(f'{RAW_DIR}/{animal.lower()}/*.txt') -> glob library

  <!-- will search for all .txt files in the specified directory and its subdirectories. -->
  recursive=True (optional parameter)
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

- lambda functions / Anonymous functions in Python:

```
lambda arguments: expression
```

```
numbers = [1, 2, 3, 4, 5]
cubes = [(lambda x: x**3)(x) for x in numbers]
print(cubes)
Output:[1, 8, 27, 64, 125]
```

<!-- similar to js array functions,these are iterable functions -->
<!-- array.map(callback) in js -->

- map(str(converts-into-string-type) or conversion function,iterables)
- filter(conversion function,iterable)
- reduce(conversion function,iterable)
- sorted(iterable, key=key(a function to decide the order), reverse=reverse(True->Descending))

```
points = [(1, 2), (3, 1), (5, -1), (2, 0)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # Output: [(5, -1), (2, 0), (3, 1), (1, 2)]
```

- sum(iterables)
- eval(string) convert string to dictionary
- strip() === trim() in js
- dictionary.items() or .values() or .keys() to iterate through dictionary
- [key,value for value in dictionary.items()]
- join and split functions
- "".join(map(str,students))
- if elif else

- random

```
<!-- With a seed: If you set a seed using random.seed(), the sequence of random numbers generated will always be the same each time the program runs, ensuring reproducibility. -->

random.seed(42)
print(random.random())  # 0.6394267984578837
print(random.randint(1, 10))  # 2
random.seed(42)
print(random.random())  # 0.6394267984578837 (same as above)
print(random.randint(1, 10))  # 2 (same as above)

```

```
random.randint(lower,higher)
<!-- randomly shuffles a list -->
random.shuffle(files)
random.sample(iterable,sample-> no. of elements to choose)
```

- os.path.join()
- .replace('.txt','.jpg',occurances=-1(default: meaning replace all occurances , you can choose 1,2,3...))
- logging library
- shutil - copying, moving, renaming, and deleting files

```
<!-- Set permissions for a file or directory -->
shutil.chmod('file_or_directory', 0o755)

shutil.copy(src,dst)

<!-- Copy an entire directory -->
shutil.copytree('source_directory', 'destination_directory')

<!-- Moving or Renaming Files -->
shutil.move('source_file.txt', 'destination_file.txt')

<!-- Deleting file -->
shutil.remove('file_to_delete.txt')
<!-- delete an empty dir -->
.rmdir
<!-- delete a non-empty dir -->
.rmtree
```
