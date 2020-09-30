# Sử dụng Comprehensions trong python

## Tables of contents
- [Sử dụng Comprehensions trong python](#sử-dụng-comprehensions-trong-python)
  - [Tables of contents](#tables-of-contents)
  - [Giới thiệu về Comprehensions](#giới-thiệu-về-comprehensions)
  - [Cú pháp](#cú-pháp)
  - [Ví dụ sử dụng comprehensions](#ví-dụ-sử-dụng-comprehensions)
  - [Kết luận](#kết-luận)

## Giới thiệu về Comprehensions

Python là ngôn ngữ lập trình rất linh hoạt và thanh lịch. Nó cho phép chúng ta làm được rất nhiều việc chỉ với một số ít dòng code. Hơn nữa, cú pháp của Python rất dễ đọc đối với con người, đó là điểm thanh lịch của Python.

Trong bài viết này, tôi sẽ giới thiệu một kỹ thuật rất hay được dùng trong python để tạo ra các cấu trúc dữ liệu như list, set, dict, đó là comprehensions. Sử dụng comprehension, ta có thể dễ dàng tạo ra các cấu trúc dữ liệu phức tạp theo cách rất tự nhiên chỉ với ít dòng code.

## Cú pháp

Cú pháp tổng quát để sử dụng comprehensions:
```
|| f(x) for x in iterable if condition ||
```
Trong đó, f(x) là hàm bất kỳ, và điều kiện if là tùy chọn. Khi sử dụng comprehensions để tạo ra một list ta gọi là list-comprehension, lúc đó cặp ký hiệu `|| ||` được thay bằng `[]`. Còn khi thay `|| ||` bằng` {} `ta có set-comprehension hoặc dictionary-comprehension.

Tóm lại, để tạo ra một list ta dùng:
```
[ f(x) for x in iterable if condition ]
```

và sử dụng cú pháp dưới đây để tạo set hoặc dict:
```
{ f(x) for x in iterable if condition }
```

## Ví dụ sử dụng comprehensions
Trong lập trình, một đoạn code đáng gía cả ngàn từ, vì vậy dưới đây tôi xin nêu ra một số ví dụ về việc sử dụng comprehensions trong Python.

Nếu ta muốn tạo một list gồm các số nguyên từ 1 đến 10, thông thường ta sẽ làm như sau:

```python
lst = []
for i in range(1,11):
	lst.append(i)

print(lst)
[1,2,3,4,5,6,7,8,9,10]
```

Với list-comprehension, ta có thể thực hiện công việc trên chỉ với một dòng code và rất dễ hiểu:

```python
lst = [i for i in range(1, 11)]

print(lst)
[1,2,3,4,5,6,7,8,9,10]

```
Nếu muốn tạo một set gồm các số nguyên trong đoạn [1..20] và chia hết cho 3, cách thông thường ta làm:

```python
s = set()
for i in range(1,21):
	if i % 3 == 0:
    	s.add(i)

print(s)
{3, 6, 9, 12, 15, 18}
```
Nhưng cực kỳ ngắn gọn với set-comprehension:

```python
s = {i for i in range(1, 21) if i % 3 == 0}

print(s)
{3, 6, 9, 12, 15, 18}
```


Thêm một ví dụ, ta muốn tạo một dict có key là các phần tử từ 1 đến 20 và gía trị là bình phương của key, trong đó ta chỉ lấy những key chia hết cho 3. Theo cách thông thường:

```python
d = {}
for k in range(1, 21):
	if k % 3 == 0:
    	d[k] = k**2

print(d)
{18: 324, 3: 9, 6: 36, 9: 81, 12: 144, 15: 225}
```

Sử dụng comprehension:
```python
d = { k: k**2 for k in range(1, 21) if k%3==0}

```
## Kết luận

Với kỹ thuật comprehensions, ta có thể tạo ra được nhiều cấu trúc dữ liệu phức tạp chỉ với những dòng code rất ngắn gọn, tự nhiên, thanh lịch và hơn nữa theo cách rất pythonic.

Nhược điểm của comprehensions đó là tất cả các phần tử sẽ được sinh ra và lưu vào bộ nhớ. Vì vậy, chỉ nên sử dụng comprehensions đối với những đối tượng có số lượng phần tử không qúa lớn. Để làm việc hiệu qủa với các đối tượng này, trong bài viết sau tôi sẽ giới thiệu về Generators.

Bài viết rất mong nhận được ý kiến và đóng góp từ các bạn, xin cảm ơn!

[Source](https://viblo.asia/p/su-dung-comprehensions-trong-python-pVYRPjJEG4ng)