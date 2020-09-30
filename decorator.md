# Function decorator trong Python

## Table of contents
- [Function decorator trong Python](#function-decorator-trong-python)
  - [Table of contents](#table-of-contents)
  - [Everything in python is object](#everything-in-python-is-object)


Python là một ngôn ngữ rất mạnh mẽ, một trong những phần quan trọng nhất của Python đó decorator. Trong ngữ cảnh của design pattern, ta có thể hiểu decorator là những functions thay đổi tính năng của một function, method hay class một cách dynamic, mà không phải sử dụng subclass. Nó rất tiện lợi khi bạn muốn mở rộng tính năng của một function mà bạn không muốn thay đổi nó. Chúng ta có thể implement decorator pattern bất nơi nào, nhưng Python tạo điều kiện cho việc đó bằng cách cung cấp nhưng tính năng và cú pháp vô cùng tiện ích.

Trong bài viết này, chúng ta sẽ cùng tìm hiểu về Python fucntion decorator, cùng với một loạt các ví dụ để làm sáng tỏ vấn đề.

Về cơ bản, decorator hoạt động như một wrapper, thay đổi hành vi của một đoạn code trước và sau khi một target function được thực thi mà không phải thay đổi chính target function, tăng cường chức năng ban đầu bằng cách decorating nó.

## Everything in python is object

Trước khi đi sâu vào tìm hiểu decorator, ta cần ôn lại một vài kiến thức về Python. Trong Python, function cũng là object và chúng ta có thể làm được nhiều thứ với function. 

- **Gán cho nó bằng một biến**

    ```python
    def greet(name):
    return "hello "+name

    greet_someone = greet
    print greet_someone("John")

    # Outputs: hello John
    ```

[Source](https://viblo.asia/p/function-decorator-trong-python-gDVK2QDe5Lj)