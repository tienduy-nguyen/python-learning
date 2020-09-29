# lambda Parameter: Operation(parameter)
lambda x: x+1

# Equivalence
def plus(x):
  return x +1

lambda x, y: x*y

# Equivalence
def mul(x, y):
  return x*y

# Example
nums = [[10, 20, 11], [3, 9, 6], [8, 14, 3]]
 
# Sort from the second value in sub array
sorted(nums, key=lambda x: x[1], reverse = True)


# Ex2: sort descrease of value in dictionaries
dic = [{'name': 'Hana', 'age': 20}, {'name': 'John', 'age': 30}, {'name': 'Karin', 'age': 22}]
sorted(dic, key=lambda x: x['age'], reverse= True)

# Ex3 : get max value in list
num3 = ['1', '100', '111', '2', 2, 2.57]
max(nums, key=lambda x: int(x))


# lambda with filter
# Ex filter the odd value in tuple
lst = (10,22,37,41,100,123,29)
oddList = tuple(filter(lambda x: (x%2 !=0), lst))
print(oddList)

# lambda with map
lst2 = (10,20,30,40,50,60)
square_list = list(map(lambda x: x**2, lst2))
print(square_list)