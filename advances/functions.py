# Map in python
# As select() in javascript, map() in ruby
nums = [1,2,3,4]
nums_double = [num * 2 for num in nums]
nums_double2 = list(map(lambda x: x*2, nums))


# Filter function
# as filter() javascript, select() in ruby
seq = [0, 1, 2, 3, 5, 8, 13]
def check(seq):
  checked = []
  for s in seq:
    if s%2 == 0:
      checked.append(s)
  return checked
print(checked(seq))
seq_checked = tuple(filter(lambda x: (x%2==0), seq))


# Reduce function
# as reduce() in JS and Ruby
num2 = [4,3,2,1]
factorial = 1
for num in num2:
  factorial *= num
print(factorial)

# Using reduce
from functools import reduce
fact = reduce(lambda fac, item: (fac*item), num2)