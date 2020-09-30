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
  - [Modules](#modules)
  - [Classes](#classes)


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


## Modules
- A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
  ```python
  # Core modules
  import datetime
  from datetime import date
  import time
  from time import time

  # Pip module
  # import camelcase
  # from camelcase import CamelCase

  # Import custom module
  import validator
  from validator import validate_email

  # today = datetime.date.today()
  today = date.today()
  timestamp = time()

  # c = CamelCase()
  # print(c.hump('hello there world'))

  email = 'test@test.com'
  if validate_email(email):
    print('Email is valid')
  else:
    print('Email is bad')
  ```
**[⬆ back to top](#table-of-contents)**

## Classes
- A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
- Create class
  ```python
  # Create class
  class User:
    def __init__(self, name, email, age):
      self.name = name
      self.email = email
      self.age = age
    def __repr__(self)
      return self.name
    def greeting(self):
      return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
      self.age += 1  
  A = User('Tim', 'tim@gmail.com', 26)
  A.has_birthday()
  print(A.greeting)
  ```
- OOP: inherit class (extend class)
  ```python
  class Customer(User):
      def set_balance(self, balance):
        self.balance = balance

      def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'
  ```
- Property, class method, static method in class
  ```python
  class Person:
    count = 0

    def __init__(self, fname='', lname='', age=18):
        self.fname = fname
        self.lname = lname
        self.age = age
        Person.count += 1

    def print(self):
        print(f'{self.fname} {self.lname} ({self.age} years old)')

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'

    @classmethod
    def print_count(cls):
        print(f'{cls.count} objects created')

    @staticmethod
    def birth_year(age: int) -> int:
        from datetime import datetime as dt
        year = dt.now().year
        return year - age


    class Student(Person):
        def __init__(self, fname='', lname='', age=18, group='', specialization=''):
            super().__init__(fname, lname, age)
            self.group = group
            self.specialization = specialization

        def print(self):
            super().print()
            print(f'Group {self.group}/{self.specialization}')

        @property
        def academic_info(self):
            return f'Group {self.group}, Specialization of {self.specialization}'


    if __name__ == '__main__':
        trump = Student('Donald', 'Trump', 22, '051311', 'Computer science')
        trump.print()
        print(trump.full_name)
        print(Student.count)
        Student.print_count()
        print(Student.birth_year(37))
        print(trump.academic_info)
  ```

  Result:
  ```
  Donald Trump (22 years old)
  Group 051311/Computer science
  Donald Trump
  1
  1 objects created
  1983
  Group 051311, Specialization of Computer science
  ```

  Check more at [tuhocit](https://tuhocict.com/ke-thua-inheritance-trong-python/)
- Name mangling & Inherit

  When in doubt, leave it "public" - I mean, do not add anything to obscure the name of your attribute. If you have a class with some internal value, do not bother about it. Instead of writing:


  ```python
  class Stack(object):

    def __init__(self):
        self.__storage = [] # Too uptight

    def push(self, value):
        self.__storage.append(value)
  ```
  write this by default:

  ```python
  class Stack(object):

    def __init__(self):
        self.storage = [] # No mangling

    def push(self, value):
        self.storage.append(value)
  ```

  Ex: add 2 attributes in class
  ```python
  self._protected = True
  self.__private = True
  ```
  try to call them
  ```
  trump = Student('Donald', 'Trump', 22, '051311', 'Computer science')
  print(trump._protected) # True
  print(trump.__private) # lỗi
  ```
- Polimophism
  
**[⬆ back to top](#table-of-contents)**