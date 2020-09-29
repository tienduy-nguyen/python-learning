'''

# Sử dụng generator : generator là một iterable, một dạng iterable
# nhưng khác ở chỗ bạn không thể tái sử dụng. 
# Bạn có một function trả về một list các phần tử, 
# nếu số phần tử trong list đó nhỏ không vấn đề gì, 
# nếu số phần tử lớn điều này sẽ là một vấn đề cho bộ nhớ. 
# Yield giúp ta giải quyết vấn đề này. 
# Lệnh này gần giống với return tuy nhiên return trả về một object 
# còn yield thì trả về một generator. 

# Mình sẽ giải thích sự khác nhau giữa return và yield :

# + Dùng return, khi được gọi một hàm sẽ thực hiện các xử lý và 
# chẳng hạn thực hiện sinh ra một list sau đó gọi return để trả về list 
# này sau khi đã thực hiện xong.

# Còn yield thì sao, khi gọi hàm những dòng lệnh bên 
# trong không được thực hiện ngay tức thì nó sẽ trả về một generator,
# và khi bạn yêu cầu nó mới bắt đầu thực hiện các dòng lệnh 
# cho đến khi lệnh yield nó trả lại giá trị và tạm dừng 
# (giữ nguyên trạng thái đang xử lý). 
# Sau đó bạn lấy giá trị trả về, yêu cầu giá trị 
# tiếp theo nó lại tiếp tục thực hiện và cứ như thế trả về 
# lần lượt thay vì thực hiện hết các vòng lặp và trả về một 
# list cuối cùng tất cả các kết quả.

'''

# Using return
nums = [16,9,4,1]
def square(nums):
  result = []
  for num in nums:
    result.append(num * num)
print(square(nums))

# Using yeild
def square2(nums):
  for num in nums:
    yield num * num
for num in square2(nums):
  print(num)

'''
YIELD thường được sử dụng trong deeplearning 
khi ta muốn ném lần lượt từng khối dữ liệu vào model 
(do dữ liệu đôi khi rất nặng, tính bằng Gb nên 
nếu ta thực hiện xử lý tất cả xong mới ném vào model 
thì quả là một điều khủng khiếp cho memory).
'''

