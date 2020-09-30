# Python iterator & generator

- [Python iterator & generator](#python-iterator--generator)
  - [Iterator](#iterator)
  - [Interation](#interation)
  - [Itertools](#itertools)
  - [Generator](#generator)
  - [Generator expression](#generator-expression)
  - [Why should use generator](#why-should-use-generator)
    - [Simplify code](#simplify-code)
    - [Increase performance](#increase-performance)


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

## Generator

- Generator là cách đơn giản để tạo ra iterator. Một generator là một hàm trả kết quả về là một chuỗi kết quả thay vì một giá trị duy nhất.
```python
def yrange(n):
  i = 0
  while i < n:
      yield i
      i += 1
```

- Mỗi lần lệnh yield được chạy, nó sẽ sinh ra một giá trị mới. (Vì thế nó mới được gọi là generator)
  ```python
  >>> y = yrange(3)
  >>> y
  <generator object yrange at 0x7f80c2f816d0>
  >>> y.__next__()
  0
  >>> y.__next__()
  1
  >>> y.__next__()
  2
  >>> y.__next__()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration
  ```
- Một generator cũng là một iterator nên bạn không cần phải lo lắng về giao thức iteration.
  
  `Từ generator được sử dụng cho cả hàm (hàm generator là hàm đã nói ở trên) và kết quả mà hàm đó sinh ra (đối tượng được hàm generator sinh ra cũng được gọi là generator). Vì vậy đôi khi việc này gây khó hiểu một chút.`
- Vậy một generator hoạt động như thế nào? Khi hàm generator được gọi, nó trả kết quả là một đối tượng generator và không thực sự gọi và thực thi hàm. Khi phương thức __next__ được gọi, hàm generator sẽ bắt đầu chạy, cho tới khi nó gặp lệnh yield. Giá trị được yield sẽ được trả về cho hàm __next__.
- Ví dụ dưới đây minh họa quá trình tương tác giữa yield và __next__ trong một đối tượng generator.
  ```python
  >>> def foo():
  ...     print("begin")
  ...     for i in range(3):
  ...         print("before yield", i)
  ...         yield i
  ...         print("after yield", i)
  ...     print("end")
  ...
  >>> f = foo()
  >>> f.__next__()
  begin
  before yield 0
  0
  >>> f.__next__()
  after yield 0
  before yield 1
  1
  >>> f.__next__()
  after yield 1
  before yield 2
  2
  >>> f.__next__()
  after yield 2
  end
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration
  ```
- Dưới đây là một ví dụ khác:
  ```python
  def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

  def squares():
      for i in integers():
          yield i * i

  def take(n, seq):
      """Returns first n values from the given sequence."""
      seq = iter(seq)
      result = []
      try:
          for i in range(n):
              result.append(seq.__next__())
      except StopIteration:
          pass
      return result

  print(take(5, squares()))

  # prints [1, 4, 9, 16, 25]
  ```
## Generator expression
- Biểu thức generator là một biến thể của list comprehension. Nó trông rất giống list comprehension nhưng nó trả về một generator thay vì một list.
  ```python
  >>> a = (x * x for x in range(10))
  >>> a
  <generator object <genexpr> at 0x7f07242b16d0>
  >>> sum(a)
  285
  ```
- Chúng ta có thể sử dụng biểu thức generator như tham số của một số hàm đối với iterator:
  ```python
  >>> sum((x * x for x in range(10)))
  285
  ```
- Nếu chỉ có một generator được truyền vào hàm, thì chúng ta có thể bỏ bớt dấu ngoặc của biểu thức generator:
  ```
  >>> sum(x * x for x in range(10))
  285
  ```
- Một ví dụ rất thú vị khác. Giả sử chúng ta cần tìm n bộ ba số Pythagoras. Một bộ 3 số (x, y, z) được gọi là bộ ba số Pythagoras nếu x*x + y*y = z*z.
  ```python
  >>> pyt = ((x, y, z) for z in integers()
  ...        for y in range(1, z)
  ...        for x in range(1, y)
  ...        if x * x + y * y == z * z)
  ...
  >>> take(10, pyt)
  [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (15, 20, 25), (7, 24, 25), (10, 24, 26), (20, 21, 29)]
  ```
## Why should use generator
### Simplify code
  - Đơn giản hóa code là một kết quả của hàm và biểu thức generator. Để minh họa cho việc này, chúng ta sẽ lấy một ví dụ cụ thể.

    Chúng ta sẽ so sánh việc cài đặt hàm firstn (hàm trả về n số nguyên không âm đầu tiên) với n có thể rất lớn và giả sử rằng mỗi số cần một lượng bộ nhớ tương đối nhiều.

    Đầu tiên, một cách làm thông thường đó là sử dụng list:
    ```python
    def firstn(n):
      num, nums = 0, []
      while num < n:
          nums.append(num)
          num += 1
      return nums

    sum_of_first_n = sum(firstn(1000000))
    ```

  - Đoạn code trên đơn giản và dễ hiểu. Tất nhiên là nó hoạt động tốt, ngoại trừ một vấn đề nhỏ là nó lưu toàn bộ list trong bộ nhớ. Trong phần lớn các trường hợp, điều đó là không hay khi phải sử dụng đến dung lượng bộ nhớ lớn đến vậy.

    Bây giờ, chúng ta thử sử dụng iterator. Dưới đây là một cài đặt cho việc này.

    ```python
    class firstn(object):

      def __init__(self, n):
          self.n = n
          self.num, self.nums = 0, []

      def __iter__(self):
          return self

      def __next__(self):
          if self.num < self.n:
              cur, self.num = self.num, self.num + 1
              return cur
          else:
              raise StopIteration()

    sum_of_first_n = sum(firstn(1000000))
    ```

  - Đoạn code trên đã hoạt động như chúng ta mong muốn, nhưng nó có một số vấn đề như:

    - Có nhiều mẫu dựng sẵn được sử dụng
    - Logic được thể hiện một cách phức tạp
    - Code mới quá dài chỉ để xây dựng một iterator
  - Chúng ta có thể sử dụng generator để xây dựng iterator ngắn gọn hơn. Chúng ta có thể cài đặt như sau:

    ```python
    def firstn(n):
      num = 0
      while num < n:
          yield num
          num += 1

    sum_of_first_n = sum(firstn(1000000))
    ```

    `Hàm firstn ở trên chỉ là một ví dụ minh họa. Python có hàm dựng sẵn là range hoạt động tương tự như vậy. Tất nhiên là thực tế chúng ta nên sử dụng hàm dựng sẵn này.`

### Increase performance
- Việc sử dụng generator có thể nâng cao hiệu suất bởi vì generator chỉ thực sự sinh kết quả khi được gọi. Do đó, nó sẽ sử dụng ít bộ nhớ hơn. Ngoài ra, chúng ta không cần phải chờ tất cả các phần tử của nó được sinh ra hết mới có thể sử dụng. Chúng sẽ được sinh trong quá trình chúng ta gọi generator. Đây là những hiệu quả đạt được khi chúng ta sử dụng iterator, mà generator là cách ngắn gọn để tạo ra một iterator.
- Để minh họa, chúng ta sẽ so sánh hai hàm dựng sẵn của Python 2 là range và xrange.

  Cả range và xrange đều biểu thị một khoảng các số nguyên. Tuy nhiên, range trả về một list còn xrange trả về một generator.

  Bây giờ, chúng ta sẽ tính tổng của 1 triệu số nguyên không âm đầu tiên.
    ```python
    # using non-generator

    sum_of_first_n = sum(range(1000000))

    # using generator

    sum_of_first_n = sum(xrange(1000000))
    ```

  Hai dòng code trông khá giống nhau. Tuy nhiên việc sử dụng range tốn bộ nhớ và thời gian hơn.

  Khi chúng ta sử dụng range, nó sẽ xây dựng list 1 triệu phần tử và sau đó tính tổng của chúng. Việc này rất lãng phí bộ nhớ vì chúng ta chỉ cần tính tổng của chúng mà thôi. Sự lãng phí càng tăng lên khi số lượng phần tử tăng lên và kích thước mỗi phần tử cũng lớn hơn.

  Vì những lợi ích của generator mà trong Python 3, hàm range hoạt động giống với xrange của Python 2, tức là nó sẽ trả về generator chứ không phải là list.

  Lưu ý đặc điểm của iterator là nó chỉ duyệt qua một lần, nên việc sử dụng generator sẽ đem lại hiệu quả **nếu chúng ta không có nhu cầu duyệt nó nhiều hơn 1 lần.**

  Hãy xem xét ví dụ sau:

    ```python
    a = sum(xrange(1000000))
    p = product(xrange(1000000))
    ```

  Giả sử rằng việc sinh một số rất tốn thời gian và bộ nhớ, thì trong ví dụ trên, chúng ta đã thực hiện công việc tốn kém này 2 lần. Trong trường hợp này, việc sử dụng list và lưu sẵn trong bộ nhớ có vẻ hiệu quả hơn.

    ```python
    nums = list(xrange(1000000))
    a = sum(nums)
    p = product(nums)
    ```

[Source](https://viblo.asia/p/python-iterator-generator-gVQelQJVkZJ)