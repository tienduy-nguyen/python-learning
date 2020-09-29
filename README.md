# Python Fundamentals & essentials

## Table of contents
- [Python Fundamentals & essentials](#python-fundamentals--essentials)
  - [Table of contents](#table-of-contents)
  - [Comments](#comments)
  - [Variables](#variables)
  - [Strings](#strings)
  - [List](#list)
  - [Tuple](#tuple)
  - [Set](#set)
  - [Dictionaries](#dictionaries)
  - [Functions](#functions)
  - [Conditionals](#conditionals)
  - [Loops](#loops)


## Comments
- We are two types of comments in python
  ```python
  # A variable is a container for a value, which can be of various types

  '''
  This is a 
  multiline comment
  or docstring (used to define a functions purpose)
  can be single or double quotes
  '''
  ```
## Variables

- Data types: `int, float, str, bool`
  ```python
  x = 1
  y = 1.5
  name = 'John'
  is_cool = True
  ```
- Multi assignement
  ```python
  x, y , name, is_cool = (1, 1.5, 'John', True)
  ```
- Basic math
  ```python
  a = x + y
  ```
- Casting
  ```python
  x = str(x)
  y = int(y)
  z = float(y)
  ```
- Check type
  ```python
  print(type(y))
  ```
**[⬆ back to top](#table-of-contents)**

## Strings

- Concatenate string
  ```python
  name='Tien Duy'
  age=26
  print('Hi, I am '+name+ ' and I am ' + age)
  ```
- String formatting
  ```python
  # Argument by position
  print('My name is {name} and I am {age}', format(name=name, age=age))

  # String literal with F-String (3.6+)
  print(f'Hello, my name is {name} and I am {age}')
  ```
- String methods
  - Capitalize
    ```python
    s = 'hello there world'
    print(s.capitalize())
    ```
  - Uppercase
    ```python
    print(s.upper())
    ```
  - Swap case
    ```python
    print(s.swapcase())
    ```
  - Lower case
     ```python
    print(s.lower())
    ```
  - Get length
     ```python
    print(len(s))
    ```
  - Replace
    ```python
    print(s.replace('world', 'everyone'))
    ```
  - Count
    ```python
    sub = "h"
    print(s.count(sub))
    ```
  - Starts with
    ```python
    print(s.startswith('hello'))
    # -> true
    ```
  - End with
    ```python
    print(s.endswith('hello'))
    ```
  - Split into a list
    ```python
    print(s.split())
    ```
  - Find position
    ```python
    print(s.find('r'))
    ```
  - Is all alphanumeric
    ```python
    print(s.isalnum())
    ```
  - Is all alphabetic
    ```python
    print(s.isalpha())
    ```
  - Is all numeric
    ```python
    print(s.isnumeric())
    ```
  - Reverse string
    ```python
    # [start:stop:stepover]
    print(s[::-1])
    print(s[:5:-1])
    print(s[:5:1])
    print(s[:5:3])
    print(s[:1:-1])
    ```
**[⬆ back to top](#table-of-contents)**

## List
- A list in python is a collection which is ordered and changeable. Allows duplicate members
- Create list
  ```python
  numbers = [1,2,3,4,5,6]
  fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

  # Or we can use constructor
  numbers2 = list[1, 2, 3, 4, 5]

  ```
- Get item of list by index
  ```python
  print(fruits[1])
  ```
- Get length
  ```python
  print(len(fruits()))
  ```
- Append a list
  ```python
  fruits.append('Mangos')
  ```
- Remove from list
  ```python
  fruits.remove('Grapes')
  ```
- Insert into position
  ```python
  fruits.insert(2, 'Strawberries')
  ```
- Change value
  ```python
  fruits[0] = 'Blueberries'
  ```
- Remove from position
  ```python
  fruits.pop(3)
  ```
- Reverse list
  ```
  fruits.reverse()
  ```
- Sort list
  ```
  fruits.sort()
  ```
- Sort list reverse
  ```
  fruits.sort(reverse=True)
  ```
- Sort by key
  ```python
  # We will use lambda
  dir =["A1","A2","A10","A3"]
  sorted(dir, key=lambda x: int(x[1:]))
  ```
**[⬆ back to top](#table-of-contents)**

## Tuple

- A tuple is a collection which is ordered and unchangeable. Allows duplicate members
- Create tuple
  ```python
  # Create tuple
  fruits = ('Apples', 'Oranges','Grapes')
  fruits2 = tuple(('Apples', 'Oranges','Grapes'))
  
  # Single value needs trailing comma
  fruits3 = ('Apple',)

  # Get value
  print(fruits[1])

  # Get length
  print(len(fruits))

  ```
- Tuple can't change value
- Delete tuple
  ```python
  del fruits2
  ```
**[⬆ back to top](#table-of-contents)**

## Set
- Set is a collection which is unordered and unindexed. Not duplicate members
- Create set
  ```python
  fruits_set =  {'Apple', 'Orange', 'Mango'}

  # Check if in set
  print('Apple' in fruits_set)

  # Add to set
  fruits_set.add('Grape')

  # Remove from set
  fruits_set.remove('Grape')

  # Delete set
  del fruits_set
  ```
**[⬆ back to top](#table-of-contents)**

## Dictionaries
- A dictionary is a collection which is unordered, changeable and indexed. No duplicate
- Create dictionary
  ```python
  person = {
    'first_name': 'Adam',
    'last_name': 'Levil',
    'age': 20
  }

  # Or use contructor
  person1 = dict(first_name='Adam', last_name='Levil', age=20)

  ```
- Get value
  ```python
  print(person['first_name'])
  print(person['last_name'])
  print(person.get('first_name', default=None))
  ```
- Add key/value
  ```python
  person['phone']='555-555-5555'
  ```
- Get dict keys
  ```python
  print(person.key())
  ```

- Get dict items
  ```python
  print(person.items())
  ```
- Copy dict
  ```python
  person2 = person.copy()
  ```
- Remove item
  ```python
  del(person['age'])
  person.pop('phone')
- Get length
  ```python
  print(len(person))
  ```
- Clear
  ```python
  person.clear()
  ```
- List of dict
  ```python
  people = [{
    {'name': 'Martha', 'age': 20},
    {'name': 'Karen', age:22}
  }]
  ```
- Check key
  ```python
  person.has_key('first_name') #-> True, False

  d = {"key1": 10, "key2": 23}

  if "key1" in d:
      print("this will execute")

  if "nonexistent key" in d:
    print("this will not")
  ```
- Built in functions for dictionary
  ```python
  cmp(dict1, dict2) # Compare two dict
  str(dict) # 
  type(variable)
  ```
**[⬆ back to top](#table-of-contents)**

## Functions

- Create a function
  ```python
  def sayHello(name= 'Sam'):
    print(f'Hello {name}')
  
  sayHello('Karen')
  ```
- Return values
  ```python
  def getSum(num1, num2):
    total = num1 + num2
    return total
  num = getSum(2, 3)
  print(num)
  ```
- Lambda function (anonymous function)
  ```python
  getSum = lambda num1, num2: (num1+num2)
  print(getSum(10, 2))
  ```

**[⬆ back to top](#table-of-contents)**


## Conditionals

- Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
  ```python
  x = 10
  y = 50
  if x > y:
    print(f'{x} is greater than {y}')
  elif x == y:
    print(f'{x} is equal {y}')
  else:
    print(f'{x} is lower than {y}')
  ```
- Nested if
  ```python
  if x > 2:
    if x <= 10:
      print(f'{x} is less than 2 and greater than 10')
  ```
- Logical or, and or not
  ```python
  # and
  if x > 2 and x <=10:
    print(f'{x} is less than 2 and greater than 10')

  # or
  if x > 2 or x <=10:
    print(f'{x} is less than 2 or greater than 10')

  # not
  if not(x == y):
    print(f'{x} is not equal to {y}')
  var = False
  if not var:
      print 'learnt stuff'
  ```
- Membership Operators (not, not in)
  
  Membership operators are used to test if a sequence is presented in an object
  ```python
  # in
  if x in numbers:
    print(x in numbers)

  # in
  if x not in numbers:
    print(x in numbers)
  ```
- Identity Operators (is, is not)
  Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
  ```python
  if x is y:
    print(x is y)
  ```
**[⬆ back to top](#table-of-contents)**

## Loops
- Simple for loop
  ```python
  for person in people:
    print(f'Current person: {person}')
  ```
- Using break in loop
  ```python
  for person in people:
    if person == 'Sarah':
      break
    print(f'Current person: {person}')
  ```
- Using continue
  ```python
  for person in people:
    if person == 'Sarah':
      continue
    print(f'Current person: {person}')
- range
  ```python
  for i in range(len(people)):
    print(people[i])
  for i in range(0, 11):
    print(f'Number: {i}')
  ```
- while loop
  ```python
  count = 0
  while count <= 10:
    print(f'Count: {count}')
    count += 1
  ```
**[⬆ back to top](#table-of-contents)**