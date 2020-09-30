# Functional Programming với Python

## Table of contents
- [Functional Programming với Python](#functional-programming-với-python)
  - [Table of contents](#table-of-contents)
  - [Itertools](#itertools)
    - [chain()](#chain)
    - [zip()](#zip)
    - [islice()](#islice)
    - [map()](#map)
  - [Lambda()](#lambda)
  - [Comprehensions](#comprehensions)

**Lập trình hàm (Functional Programming) là gì?**
  Lập trình hàm là một trường phái trong đó coi hàm (không phải object) là các khối nền tảng để xây dựng chương trình, với ý tưởng ta có thể truyền hàm như là tham số tới các hàm khác và có thể trả về chúng như gía trị. Lập trình hàm liên quan đến việc viết code không thay đổi trạng thái. Lý do chính là các lời gọi hàm liên tiếp sẽ cho ra cùng kết qủa. Ta có thể dùng lập trình hàm với bất kỳ ngôn ngữ nào hỗ trợ first-class functions. Một số ngôn ngữ như Haskell, không cho phép thay đổi trạng thái (ví dụ: các thao tác vào ra).

**Lợi thế lập trình hàm mang lại?**
  Functional programming giúp code ít lỗi hơn do mỗi thành phần đọc lập hoàn toàn với nhau. Hơn nữa, code sẽ dễ đọc hơn bởi vì cú pháp giống các biểu thức toán học.

**Lập trình hàm với Python**
  Trong phần này, ta sẽ cũng làm quen với một vài functions cho phép lập trình theo phong cách functional trong ngôn ngữ Python. Code trong bài viết sử dụng với python 3.

## Itertools

Hãy bắt đầu với khái niệm nền tảng quan trọng cho việc lập trình hàm trong python: iterators. Đây là đối tượng biểu diễn dòng dữ liệu và trả về từng phần tử một. Iterator cực kỳ hữu dụng khi thao tác với lists, tuples, strings, ..., etc. Các hàm cung cấp bởi itertools bắt chước các tính năng tương tự của các ngôn ngữ lập trình hàm như Clojure và Haskell, được tối ưu về tốc độ và bộ nhớ.

### chain()
  Hàm chain() nhận đầu vào là các iterators và xâu chuỗi lại thành một iterator duy nhất.

  ```python
  from itertools import chain

  l1 = [1, 2, 3]
  l2 = [4, 5, 6]
  l3 = [7, 8, 9]
  for i in chain(l1, l2, l3):
      print(i) # 1,2,3,4,5,6,7,8,9

  print(list(chain(l1, l2, l3))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(sum(chain(l1, l2, l3))) # 45


  # Normal methods
  listone = [1,2,3]
  listtwo = [4,5,6]

  joinedlist = listone + listtwo
  joined_list2 = [*l1, *l2]  # unpack both iterables in a list literal
  ```
### zip()
  Tạo ra một iterator kết hợp các phần tử từ iterators khác. zip() có đặc tính lazy, nghĩa là nó chỉ tính toán các phần tử khi được yêu cầu.

  ```python
  lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  for i in zip(*lst):
      print(i)
  # (1, 4, 7)
  # (2, 5, 8)
  # (3, 6, 9)
  ```
### islice()
Hàm này trả về một iterator theo cách thức tương tự như slice, iterable[start:stop:step]. Khác với slice, start, stop, step không được nhận gía trị âm.

```python
from itertools import islice
a = range(10)
i = iter(a)
print(list(islice(i, 1, 3))
print(list(islice(i, 1, 3))
print(list(islice(i, 1, 3))
print(list(islice(i, 1, 3))
#[1, 2]
#[4, 5]
#[7, 8]
#[]
```
### map()
Trả về một iterator cho ra các phần tử function(i1, i2, ..., iN), trong đó i1, i2, ..., iN là các phần tử được lấy ra từ các iterators iter1, iter2, ..., iterN tương ứng. Nếu function là None, hàm sẽ trả về các tuples có dạng (i1, i2, ..., iN).

```python
from operator import add

print([i for i in map(pow, (2,3,10), (5,2,3))])
# [32, 9, 1000]

print([i for i in map(add, map(pow, (2,3,10), (5,2,3)), (2,2,2))])
# [34, 11, 1002]
```
## Lambda()

Python hỗ trợ tạo hàm động không tên hay còn gọi là anonymous functions, bằng cách sử dụng lambda. Tuy không đầy đủ như lambda trong các ngôn ngữ functional nhưng đây cũng là một kỹ thuật mạnh mẽ được tích hợp tốt trong Python và thường được sử dụng kết hợp với các khái niệm functional điển hình như filter(), map() và reduce().

Cú pháp xậy dựng anonymous functions:

`lambda args: expression`

Trong đó, args là danh sách (được ngăn cách bởi dấu phẩy ",") các tham số và expression là một biểu thức theo các tham số trên. Đoạn code dưới đây chỉ ra sự khác nhau giữa một hàm thông thường và anonymous functions:

```python
def square(x):
    return x*x
print(square(4)) # 16

#----------------------#
square = lambda x: x*x
print(square(4)) # 16
```

Như bạn thấy, cả 2 hàm square() cùng thực hiện một chức năng và lời gọi hàm là giống nhau. Lưu ý rằng lambda không chứa câu lệnh return - nó luôn chứa một expression được trả về. Hơn nữa, bạn có thể đặt lambda functions bất cứ nơi đâu mà bạn muốn, không cần nhất thiết phải gán tên cho nó.

## Comprehensions

See more at [comprehensions of python](comprehensions-python.md)


[Source](https://viblo.asia/p/functional-programming-voi-python-WApGx3AYM06y)