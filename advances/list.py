# Manipulation with list in python

# Reverse list
elems = list(range(10))
eReverse = elems[::-1]

# Replace multi item in array
elem2 = list(range(3))
print(elem2)
elems[:1] = [5,5,66]
print(elem2)
# -> [0,1,2]
# -> [5,5,66,1,2]
