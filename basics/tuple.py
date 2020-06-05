# Tuple as a list but it is immutable
myTuple = (1,2,3,4,5,6)

print(myTuple[0])
print(myTuple.index(5))
print(5 in myTuple)
for i in myTuple:
    print(i)

# myTuple[0]=10 --> get an error because the tuple is immutable
# Tupple su dung dau ngoac tron ()
# Con list su dung dau []
# Dictionary su dung dau ngoac nhon {}
class Point:
     def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
     def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
p1 = Point(3, 4)
p2 = Point(1, 2)
result = p1-p2
print(result.x, result.y)

def outerFunction():
     global a
     a = 20
     def innerFunction():
          global a
          a = 30
          print('a =', a) 
a = 10
outerFunction()
print('a =', a)