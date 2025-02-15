## Knowledge Vault(Python)

- Spread operator in Python

```
* in python equivalent to ... in js when working with lists or iterables
but ** when working with dictionaries
Also,
Python has separate operator for packing func arguments like (*args) to pack functional argument in list and (**kwargs) in dictionary while js uses the same (...) spread operator to do so
```

- In Python -> arguments in python -> positional(in exact order of parameters in a function definition) and keyword(Arguments passed using the parameter name in the call)

```
# Positional argument call
# Can lead to confusion and errors if arguments are passed in the wrong order.
greet("Alice", 30)

# Keyword argument call
# Order of arguments doesn't matter.
greet(name="Alice", age=30)
```

- The `*` in the function signature is a Python feature that enforces keyword-only arguments.
  Arguments before `*` can be provided as positional or keyword arguments.
  Arguments after `*` must be provided as keyword arguments.

```
def update(
    *, db_session, conversation: Conversation, conversation_in: ConversationUpdate
):

# Enforced argument passed as keyword-arguments
update(
    db_session=session,
    conversation=my_conversation,
    conversation_in=update_data
)

```

- iterable vs iterator -> supports `__iter__()` method, Lists,strings and dictionaries -> can convert to iterator using `iter(iterable)` vs represents a stream of data, calls next item when `next()` or implements `__next()__` method

- `map`,`filter`,`next` -> array-comprehension

```
next(iterator,default)

iterator -> stream of data(generators), not iterables though
default -> default value if iterator exhausted

Eg:
# Creating an iterator from a list
my_list = [1, 2, 3, 4]
iterator = iter(my_list)

# Using next() to get the next item
print(next(iterator,"End"))  # Output: 1
print(next(iterator,"End"))  # Output: 2
print(next(iterator,"End"))  # Output: 3
print(next(iterator,"End"))  # Output: 4
print(next(iterator,"End"))  # Output: "End"

Eg: label = next((key for key, value in class_labels.items() if value == class_name), ""),
the parameter: (key for key, value in class_labels.items() if value == class_name) -> generator expression(iterator), yields value one by one
```

- `**args` and `**kwargs`

- strings in Python are immutable
- label.replace() method returns a new string, but doesn't modify the original string in place

- yield from -> like yield used in generator functions but tells the generator function to iterate over that thing(string,list,tuple) such that each part iterated, yield that part as coming from this generator function
  -> The yield from keyword is used to delegate part of the generator’s operations to another generator or iterable. This is helpful when you have nested generators or want to include another iterable in a generator.

```
def nested_generator():
yield from [1, 2, 3] # Delegates to a list
yield from range(4, 6) # Delegates to a range object

for value in nested_generator():
print(value)
// Output: 1 2 3 4 5

```

- Async Context Manager in Python -> To manage resources asynchronously
  such as connecting to databases,opening files, or acquiring locks

```

from contextlib import asynccontextmanager

@asynccontextmanager -> Converts the function into something called and "async context manager"

- A context manager in Python is something that you can use in a `with` statement. For Example open() can be used as a context manager

with open("file.txt) as f:
// code

async with lifespan(app): # block-of-code
await do_stuff() # after finishing do_stuff(), the code after yield in lifespan() will be executed

When you create a context manager or an async context manager like above, what it does is that, before entering the with block, it will execute the code before the yield, and after exiting the with block, it will execute the code after the yield.

```

Example code:

```

import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource_manager(): # Asynchronous setup code
print("Acquiring resource")
await asyncio.sleep(1) # Simulate an async operation, e.g., connecting to a database or loading a ML model
resource = "my_resource" # Replace with actual resource
try: # The yield statement allows the function to temporarily return the # resource to the caller (the block of code that uses the context # manager). The code execution will pause here until the block completes. # Yield: The yield statement provides the resource to the block of code inside the async with statement. # After yield: cleanup code.

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

await asyncio.sleep(1) # Simulate work with the resource

# Run the main function

asyncio.run(main())

```

- Decorators in Python(Wrapper over a function -> Special type of callback function -> Like Higher-Order-Function in JS): tool for modifying or extending the behavior of functions or classes. "WRAPPING" functionality around an existing function or class. Enforces DRY !!!
  Eg: @property(getter,setter for `_radius`-> protected variable)

```

class User:
def **init**(self, name, age):
self.\_name = name
self.\_age = age

    @property
    def name(self):
        return self._name

    <!-- if required to set custom setter -->
    @name.setter
    def name(self, value):
        if(value>5):
          self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

```

```

def my_decorator(func):
def wrapper(*args,\*\*kwargs): # Code to execute before the function
result=func(*args,\*\*kwargs) # Code to execute after the function
return result

return wrapper

@my_decorator
def greet():
print("Hello, World!")

```

```

*args -> Variable-Length Positional Arguments like spread operator in js {...args} -> gives the function arguments as array. Similarly *args in tuple

\**kwargs -> Variable-Length Keyword Arguments -> Similar to *args but gives out dictionary -> Eg: (name="Alice")->{name:"Alice}
kwargs.get("name")-> gets key
kwargs.pop("name") -> gets value for the corresponding key
```

- Public,Private,Protected variable in Python

```

\_variable -> protected (for internal use only, should not be accessed directly by external code)
\_\_variable -> private
variable -> public

Eg:
class Circle:
def **init**(self, radius):
self.\_radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c=Circle(5)
print(c.radius)
print(c.area)

c.radius=10
print(c.area)

```

- Inheritance in Python

```

class Parent:

# Parent class definition

pass -> Placeholder, no attributes or methods defined yet # Do nothing Function

class Child(Parent):

# Child class definition

pass

super() -> to call parent class function

```

- assert in Python: Debugging so `python -O your_script.py` to disable them in Production

```

assert x===5, "X should be equal to 5"
print("Assertion passed")

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
print(item[::2]) # Output: "hlo"

```

- all(iterable) -> Returns True or False -> equivalent to array.every(callback) in js

```

print(all(["hello", "world", ""])) # Output: False (because of the empty string)

numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers)) # Output: True (all numbers are even)

```

- Dict Comprehensions

```

numbers = [1, 2, 3, 4, 5]
even_square_dict = {x: x\*\*2 for x in numbers if x % 2 == 0}
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

glob.glob(f'{RAW_DIR}/{animal.lower()}/\*.txt') -> glob library

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
print(sorted_points) # Output: [(5, -1), (2, 0), (3, 1), (1, 2)]

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
print(random.random()) # 0.6394267984578837
print(random.randint(1, 10)) # 2
random.seed(42)
print(random.random()) # 0.6394267984578837 (same as above)
print(random.randint(1, 10)) # 2 (same as above)

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

### More Important concepts in Python

1. Generators and Iterators

- generators: type of iterable(like list and tuples) -> uses the yield keyword

Also, All generator functions are iterators because they produce values one at a time and maintain their state.

Using generators can be more memory-efficient than using lists, as they yield items one by one instead of storing the entire sequence in memory at once. This is particularly useful for large datasets or streams of data​

```

def generator_example(n):
while(n>5):
yield n
n=n-1

generate=generator(10)

for number in generate:
print(number)

Output: 10,9,8,7,6

```

- iterators: `__iter__()` and `__next__()`
  Also,All generator functions are iterators (like list and tuples) because they produce values one at a time and maintain their state.

```

class Countdown:
def **init**(self,start):
self.current=start

def **iter**(self):
return self

def **next**(self):
if self.current<=0:
raise StopIteration
else:
result=self.current
self.current-=1
return result

for number in Countdown(5):
print(number)

```

2. Context Managers

- `with` statement

Custom Context Manager

```

from contextlib import contextmanager

@contextmanager
def managed_file(filename):
try:
f=open(filename,'w)
yield f
finally:
f.close()

with managed_file('file.txt') as f:
f.write('Hello, World!')

```

3. List Comprehensions vs For Loops

squares=[x**2 for x in range(10)] -> More readable than for-loop

```

```
