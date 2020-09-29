# Some concepts must know in classes of python

# __dict__ of object
'''
This property stores all properties defined for an objet and its values in json
'''

class People:
  def __init__(self, name):
    self.name = name
    self.college = None
  def __add__(self, text):
    return self.name + text
A = People('misaka')
print(A+ 'form VN')
print(A.__dict__)

# -> {'name': 'misaka', 'college': None}


# **kwargs:
'''
When we want to pass parameters, but they can be one, two, three or multi parameters.
In this case, we will use **kwargs
'''

class People:
  def __init__(self, **kwargs):
    self.__dict__ = kwargs
A = People(name='misaka', college='VN', age='20')
print(A.__dict__)
# -> {'name': 'misaka', college: 'VN', 'age': 20}