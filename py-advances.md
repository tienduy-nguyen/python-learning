# Concepts must know in Python

## Import

- Khi bạn viết một file python và muốn import một vài function từ một file khác vào, do hơi lười nên bạn không muốn nhập một dãy tên các function, bạn sử dụng import * chẳng  hạn   from util import * 

- Trông thì có vẻ không ảnh hưởng lắm, bạn nghĩ ừ thì nó import thừa một vài function cũng chẳng sao.

- Xét một ví dụ : bạn muốn from util import *  từ một file như sau 

  ```python
  import numpy

  import tensorflow

  class Encoder:

      ...

  class Decoder:

      ...

  class Loss:

      ...

  ```
- Khi đó, dòng lệnh này không chỉ import Encoder, Decoder, Loss mà cả numpy, tensorflow. Để tránh việc dư thừa như này, người ta sử dụng keyword __all__ . Trong file trên, nếu ta thêm vào dòng  __all__ = ['Encoder', 'Decoder']  thì khi  import *  sẽ chỉ import vào 2 function là Encoder và Decoder. 

- Điều này sẽ giải quyết những dòng import "vô trách nhiệm" của bạn :D

## Decorator

- Decorator là một trong những tính năng tuyệt vời nhất của Python, tuy nhiên đối với người mới bắt đầu lập trình Python, chúng có vẻ như là phép thuật vậy. Bạn sẽ thấy cách mà decorator được viết như dưới đây:
  ```python
  @decorator 

  def function_to_decorate():

      pass
  ```
- Các bạn sẽ nhận biết nó dựa vào @, vâng đó là một decorator. Về bản chất nó là một hàm, tuy nhiên nó là một hàm phức hợp. Một decorator nhận một hàm như là một tham số đầu vào và trả về một hàm khác. Decorator được định nghĩa theo hình thức sau:
  ```python
  def decorator(funciton_to_decorate):

      # …

      return decorated_function 
  ```
- Xem ví dụ để dễ hiểu hơn nhé
  ```python
  def squared(func):
    return lambda x: func(x) * func(x)
  @squared
  def double(x):
    return 2 * x
  print(double(5))
  # -> 100
  ```
## Cache Saving

- Bộ nhớ đệm (cache) là một kỹ thuật quan trọng do đó python cung cấp một decorator giúp ta lưu lại các tính toán trước đó. 
  ```python
  import functools
  
  @functools.lru_cache()
  def double(x):
    return 2 * x
  print(double(5))
  # -> 10
  ```

  Check more functools at [official doc](https://docs.python.org/3/library/functools.html)

## Copy list

To copy the list in python, we have various possibilities:
- Use list.copy() (shadow copy)
  ```python
  new_list = old_list.copy()
  ```
- Slice it (shadow_copy)
  ```python
  new_list = old_list[:]
  ```
- Use built in list() function
  ```python
  new_list = list(old_list)
  ```
- Use generic copy.copy() (shadow copy)
  ```python
  import copy
  new_list = copy.copy(old_list)
  ```
  This is a little slower than list() because it has to find out the datatype of old_list first.
- If the list contains objects and you want to copy them as well, use generic copy.deepcopy():
  ```python
  import copy
  new_list=copy.deepcopy(old_list)
  ```
  Obviously the slowest and most memory-needing method, but sometimes unavoidable.

