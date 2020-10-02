# Regex với Python

- [Regex với Python](#regex-với-python)
  - [Thư viện](#thư-viện)
  - [Một số hàm](#một-số-hàm)
    - [re.match](#rematch)
    - [findall()](#findall)
    - [re.search](#research)
    - [re.split](#resplit)
    - [re.sub](#resub)

## Thư viện

Regex sử dụng module re để làm việc trong python, module này là thư viện built-in trong python, bạn không cần phải cài đặt để sử dụng

```
import re
```
## Một số hàm
### re.match

```python
re.match(pattern, string, flags=0)
```
So khớp pattern với string với các flag tùy ý. Dưới đây là cú pháp cho hàm này.


- **pattern** : Đây là chuỗn cần so khớp.
- **string** : Đây là chuỗi để tìm kiếm pattern cón tồn tại trong đó không.
- **flags** : Bạn có thể xác định các flag khác nhau bởi sử dụng toán tử |. 
Các modifier này sẽ được liệt kê ở bảng bên dưới.

### findall()

In ra tất cả những đoạn phù hợp

Hoặc nếu không tìm thấy kết quả nào phù hợp thì trả về một danh sách rỗng

```python
str = 'The rain in Spain'
x = re.findall('Portugal',str)
```


### re.search

```
re.search(pattern, string, flags=0)
```
Hàm này thực hiện tìm kiếm chuỗi khớp trên 1 string và trả về các giá trị được so khớp

Hoặc sẽ trả về None nếu không tìm thấy

### re.split

```python
re.split(pattern, string, maxsplit=0, flags=0)
```

re.split trả về các ký tự được phân tách nhờ đoạn pattern


### re.sub

Thay the nhung ki tu tim duoc trong pattern

```python
str = "The rain is Spain
re.sub('\s', '9', str)
```


[Source](https://viblo.asia/p/regex-voi-python-RQqKLLpzK7z)