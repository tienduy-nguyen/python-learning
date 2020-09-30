# Python iterator & generator

- [Python iterator & generator](#python-iterator--generator)
  - [Iterator](#iterator)
  - [Interation](#interation)
  - [Itertools](#itertools)


## Iterator

- Chúng ta có thể sử dụng vòng lặp for để duyệt qua các phần tử của một list:
  ```python
  >>> for i in [1, 2, 3, 4]:
  ...     print(i)
  ...
  1
  2
  3
  4
  ```
- Nếu chúng ta sử dụng for cho một string, chúng ta sẽ duyệt qua các ký tự của nó:
  ```python
  >>> for c in "python":
  ...     print(c)
  ...
  p
  y
  t
  h
  o
  n
  ```
- Nếu chúng ta sử dụng một dict, chúng ta sẽ duyệt qua các key của nó:
  ```python
  >>> for k in {"x": 1, "y": 2}:
  ...     print(k)
  ...
  y
  x
  ```
- Nếu chúng ta sử dụng một file, chúng ta sẽ duyệt qua các dòng trong file đó:
  ```python
  >>> for line in open("a.txt"):
  ...     print(line)
  ...
  first line
  second line
  ```
- Có rất nhiều đối tượng chúng ta có thể sử dụng vòng lặp for. Những đối tượng đó gọi là những đối tượng "iterable". Và thao tác duyệt qua những đối tượng này gọi là iteration.

- Có một số hàm dựng sẵn có Python cho phép thao tác với những đối tượng này:
  ```python
  >>> ",".join(["a", "b", "c"])
  'a,b,c'
  >>> ",".join({"x": 1, "y": 2})
  'y,x'
  >>> list("python")
  ['p', 'y', 't', 'h', 'o', 'n']
  >>> list({"x": 1, "y": 2})
  ['y', 'x']
  ```
- Vậy, ở sâu bên trong, Python làm thế nào để có thể duyệt qua những đối tượng này. Đó chính là điều chúng ta sẽ tìm hiểu trong phần tiếp theo đây.

## Interation

- Những đối tượng "iterable" có thể được duyệt qua các phần tử, bởi vì chúng được cài đặt phương thức __iter__. Phương thức này sẽ trả về một đối tượng iterator. Đối tượng này cần phải hỗ trợ giao thức iteration (sẽ được nói đến sau). Nếu một đối tượng "iterable" có nhiều kiểu duyệt phần tử khác nhau, có thể chúng ta sẽ cần thêm các xử lý để xác định iterator. (Ví dụ một đồ thị có thể duyệt theo chiều rộng và theo chiều sâu.)

- Với đối tượng iterator, nó cần phải được cài đặt hai phương thức sau, và bộ hai phương thức này được gọi là **giao thức iteration**.
  - Phương thức __iter__ trả về chính đối tượng iterator. Phương thức này được yêu cầu cài đặt cho cả đối tượng "iterable" và iterator để có thể sử dụng các câu lệnh for và in.
  - Phương thức __next__ (ở Python 2 là next) trả về phần tử tiếp theo. Nếu không còn phần tử nào nữa thì StopIteration exception sẽ được raise.
- Một hàm dựng sẵn của Python là iter nhận đầu vào là một đối tượng "iterable" và trả về kết quả là một iterator.
  ```python
  >>> x = iter([1, 2, 3])
  >>> x
  <list_iterator object at 0x7f24ee1a7a90>
  >>> x.__next__()
  1
  >>> x.__next__()
  2
  >>> x.__next__()
  3
  >>> x.__next__()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration
  ```
- Mỗi khi chúng ta gọi phương thức __next__ (ở Python 2 là next) thì iterator sẽ trả cho chúng ta phần tử tiếp theo của nó. Nếu không còn phần tử nào trong iterator, StopIteration sẽ được trả về.
- Chúng ta có thể tự cài đặt iterator là một class. Ví dụ dưới đây là một iterator hoạt động tương tự như hàm range có sẵn của Python.
  ```python
  class yrange:
    def __init__(self, n):
      self.i = 0
      self.n = 0
    def __iter__(self):
      return self
    def __next__(self):
      if self.i < self.n:
        i = self.i
        self.i += 1
        return i
      else:
        raise StopIteration()

  ```
- Phương thức __iter__ sẽ làm đối tượng trở thành đối tượng "iterable". Về bản chất, hàm iter sẽ gọi đến phương thức __iter__ này của mỗi đối tượng.
- Giá trị trả về của __iter__ là một iterator. Nó cần có phương thức __next__ và cần trả về StopIteration nếu không còn phần thử nào nữa.
- Try with example above
  ```bash
  >>> y = yrange(3)
  >>> y.__next__()
  0
  >>> y.__next__()
  1
  >>> y.__next__()
  2
  >>> y.__next__()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 14, in next
  StopIteration
  ```
- Trong các ví dụ trên, iterator và đối tượng "iterable" là một. Bởi vì phương thức __iter__ chỉ đơn giản là trả về self. Không phải trường hợp nào iterator và đối tượng "iterable" cũng là một, như ví dụ dưới đây:
  ```python
  class zrange:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

  class zrange_iter:

      def __init__(self, n):
          self.i = 0
          self.n = n

      def __iter__(self):

  # Iterators are iterables too

  # Adding this functions to make them so

          return self

      def __next__(self):
          if self.i < self.n:
              i = self.i
              self.i += 1
              return i
          else:
              raise StopIteration()
  ```
- Iterator của Python có một đặc điểm là nó chỉ có thể được duyệt qua 1 lần. Nên nếu đã duyệt qua phần tử nào rồi thì bạn không thể duyệt qua nó thêm lần nào nữa.

- Vì đặc điểm trên, nên nếu iterator và đối tượng "iterable" là một, thì nó cũng chỉ có thể thực hiện iteration một lần. Nhưng nếu chúng không phải là một, thì bạn có thể thực hiện bao nhiêu lần tùy ý.
  ```python
  >>> y = yrange(5)
  >>> list(y)
  [0, 1, 2, 3, 4]
  >>> list(y)
  []
  >>> z = zrange(5)
  >>> list(z)
  [0, 1, 2, 3, 4]
  >>> list(z)
  [0, 1, 2, 3, 4]
  ```

## Itertools

Module itertools là thư viện chuẩn của Python. Nó cung cấp cho chúng ta rất nhiều công cụ để làm việc với các iterator.

Trong bài viết này, chúng ta sẽ điểm qua một số hàm thú vị.

- **chain** sẽ gộp các iterator với nhau tạo thành một iterator.

  ```python
  >>> it1 = iter([1, 2, 3])
  >>> it2 = iter([4, 5, 6])
  >>> itertools.chain(it1, it2)
  <itertools.chain object at 0x7f9592192278>
  >>> list(itertools.chain(it1, it2))
  [1, 2, 3, 4, 5, 6]
  ```
- **dropwhile** trả về kết quả là một iterator từ một đối tượng "iterable" bằng cách loại bỏ các phần tử ở đầu đối tượng iterable thỏa mãn điều kiện nào đó. Kể từ lúc điều kiện được thỏa mãn, nó sẽ trả về các phần tử từ đó trở đi.
  ```python
  >>> itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])
  <itertools.dropwhile object at 0x7f46c544a708>
  >>> list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
  [6, 4, 1]
  ```

- **takewhile** có phần ngược với dropwhile, nó trả về một iterator bằng cách lấy ra các phần tử từ đối tượng "iterable" chừng nào điều kiện còn được thỏa mãn.


[Source](https://viblo.asia/p/python-iterator-generator-gVQelQJVkZJ)