'''
Trong python, các Dunder (còn gọi là magic methods) 
là các phương thức có tiền tố và hậu tố là 2 dấu gạch dưới   __ 
chẳng hạn như :  __init__, __add__,  __len__,  __repr__ 

Ở đây có lẽ các bạn sẽ quen thuộc nhất với  __init__     =))
'''

# __init__
'''
__init__ : Khi bạn tạo ra một object, phương thức __init__ 
tự động được gọi đến mà không cần bạn phải trực tiếp gọi,
để khởi tạo các thuộc tính được định nghĩa cho đối tượng.

'''
class People:
  def __init__(self, name):
    self.name = name
# Create object
A = People('mr.A')
print(A)

# __repr__
'''
__repr__: Ở đoạn mã trên khi in đối tượng A ta chỉ nhận lại địa chỉ 
trên bộ nhớ vật lý của đối tượng. 
Muốn in ra được một string để đại diện cho object ta sử dụng phương thức  __repr__
'''

class People1:
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return 'My name is {}'.format(self.name)
B  = People('mr.B')
print(B)

# __add__
# Hay kết hợp string object với people object như ví dụ dưới đây 
class People2:
  def __init__(self, name):
    self.name = name
  def __add__(self, text):
    return self.name + text
C = People('mr.C')
print(C+ 'from VN')

'''
Ngoài ra các bạn có thể tìm hiểu các dunder khác như 
__len__, __iter__, __slots__, __lt__,... để code pro hơn nhé  =))
'''

# Check explanation beetween len() and __len__
# https://stackoverflow.com/questions/2481421/difference-between-len-and-len

'''
len is a function to get the length of a collection. It works by calling an object's __len__ method. __something__ attributes are special and usually more than meets the eye, and generally should not be called directly.

It was decided at some point long ago getting the length of something 
should be a function and not a method code, 
reasoning that len(a)'s meaning would be clear to beginners 
but a.len() would not be as clear. When Python started __len__ didn't 
even exist and len was a special thing that worked with a few types of objects. 
Whether or not the situation this leaves us makes total sense, it's here to stay.
'''

# __len__
class Employee:
  name=''
  def __init__(self, n):
    self.name = n
  def __len__(self):
    return len(self.name)
e = Employee('Pack')
print('Employee object length = ', len(e))