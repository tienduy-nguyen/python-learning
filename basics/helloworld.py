print("Hello world")
num = 2.5
print(type(num))
num = 1
while num <= 10:
    print(num)
    num += 1
for i in range(1,11):
    print (i)
myInteger = range(1,10)
print('My integer 3 is : ',myInteger[3])

# Dictionary: Key value Data structure
dictionary = {
    "key1" : "value1",
    "key2" : "value2"
}
print(dictionary)
dictionary2 = {
    "name": "Diep",
    "age": 20
}
print(dictionary2["name"])
bookshelf = [
  "The Effective Engineer",
  "The 4 hours work week",
  "Zero to One",
  "Lean Startup",
  "Hooked"
]
for book in bookshelf:
    print(book)
name = "Duy"
print(f'Hello {name}\n'*5)

# Kiem tra contains trong chuoi
str1 = "NGUYENTienDuy"
print('duy'.lower() in str1.lower())
print(str1[2])
print(len('LearnWebDeveloper'))

# Cat chuoi
print(str1[3:len(str1)])
print(str1[3:None])
print(str1[5:-1])
print(str1[None:5:-1])
print(str1[None:5:2])
print(str1[None:5:2])
print(str1[None:1:-1])
print(hash(str1))
print(str1.strip("N"))

import re
 
pattern = '^a.*s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Tim kiem thanh cong.")
else:
    print("Tim kiem khong thanh cong.")

basket = [1,2,3,4,5,6]
basket.append(20)
print(basket)