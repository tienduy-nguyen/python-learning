# Multi threading in python

Trong bài viết này, tôi muốn giới thiệu với các bạn về các cơ chế, kỹ thuật đồng bộ trong lập trình đa luồng (multithreading). Các kỹ thuật được trình bày trong ngôn ngữ Python nhưng về nguyên lý đều có thể áp dụng cho các ngôn ngữ khác. Những từ khóa chính trong bài viết: multithreading, Lock, RLock, Condition, Event, Queue.

## Lập trình đa luồng trong Python

Module threading của thư viện chuẩn Python cung cấp cho chúng ta các class và function để làm việc với thread, nó cũng cung cấp các cơ chế để đồng bộ luồng, bao gồm: Thread, Lock, RLock, Condition, Semaphore,Event,...

Note: Trong Cpython, Global Interpreter Lock - GIL giới hạn chỉ có một thread được chạy tại một thời điểm, nên về cơ bản Cpython sẽ không hoàn toàn hỗ trợ đa luồng, nhưng ta có thể sử dụng các Interpreter khác (Jython và IronPython) không sử dụng GIL vì vậy có thể chạy đa luồng.

Class Thread cung cấp cho chúng ta các phương thức cần thiết để làm việc với luồng, cụ thể ta có:

- start(): Method dùng để kích hoạt (chạy) một thread object, mặc định sẽ gọi run() method.
run(): Đây là phương thức chính chúng ta cần cài đặt, mô tả các công việc mà luồng thực hiện. Mặc định phương thức này sẽ gọi hàm liên kết với đối số target lúc khởi tạo luồng.
- join(): Khi được gọi, method này sẽ block thread gọi nó (calling thread) cho đến khi thread được gọi (called thread - tức là thread có method join() vừa gọi) kết thúc. Method này thường được dùng trong luồng chính để đợi các thread khác kết thúc công việc của mình và xử lý tiếp kết qủa.
- Ngoài ra class Thread còn cung cấp thêm một số thuộc tính và phương thức nữa như là: name, getName(), setName(),... Bạn có thể tham khảo thêm tại [1](https://docs.python.org/3.5/library/threading.html#thread-objects)
  
Để tạo một luồng mới với class Thread, ta có 2 cách:

- Truyền hàm cần thực hiện thông qua tham số target lúc khởi tạo Thread object.
- Kế thừa class Thread và cài đặt method run()

Đoạn code dưới đây minh họa 2 cách tạo create như trên:

```python
import threading
import math

def target_func(data):
	thread_id = threading.get_ident()
	print('Thread {} is running with data: {}'.format(thread_id, data))

class WorkerThread(threading.Thread):
	def __init__(self, data):
    	super().__init__()
        self.data = data # Initiliaze data for thread

	def run(self):
    	# This method is invoked when starting a thread
        # Do the work of thread here.
        print('Thread {} is running with data: {}'.format(self.ident, self.data))

if __name__ == '__main__':
	a = 'goodkat'
    b = 'godfather'

    # Create thread by passing target_func to target param
    thread1 = threading.Thread(target=target_func, args=(a,))

    # Or by using CheckPrimeThread
    thread2 = WorkerThread(b)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for thread1, thread2 to terminate
    thread1.join()
    thread2.join()

    print('Main thread exited')

# Output:
# Thread 140280251209472 is running with data: goodkat
# Thread 140280242816768 is running with data: godfather
# Main thread exited
```

## Các cơ chế đồng bộ trong Python


Trong phần này, tôi sẽ trình bày về các cơ chế đồng bộ trong lập trình đa luồng thông qua bài toán đếm số nguyên tố: Cho số nguyên dương N, liệt kê ra các số nguyên tố trong đoạn từ 2 đến N.

Nếu giải bài toán này theo cách tuần tự (đơn luồng) thông thường thật đơn giản. Chỉ cần cài đặt hàm kiểm tra một số đầu vào có là số nguyên tố hay không, sau đó kiểm tra từng số trong đoạn từ 2 đến N, nếu là số nguyên tố thì in ra màn hình.

Trong lập trình đa luồng, có 3 yếu tố ta cần phải quan tâm đó là:

- Chia nhỏ bài toán: Chia nhỏ khối lượng công việc cần tính toán và giao cho mỗi luồng thực hiện riêng một phần công việc đó.
- Cân bằng tải giữa các luồng: Ta cần đảm bảo khối lượng tính toán mà mỗi luồng phải thực hiện càng bằng nhau càng tốt.
- Đồng bộ giữa các luồng khi các luồng chia sẻ tài nguyên với nhau: Ta cần đảm bảo tính toàn vẹn của dữ liệu khi có nhiều luồng đồng thời truy cập vào dữ liệu chung.

Chia nhỏ bài toán: Trong bài toán trên, ta có 2 cách để chia nhỏ bài toán:

- Chia dãy số từ 2 -> N thành các đoạn, nếu chương trình có K luồng, thì ta sẽ có K đoạn (có số lượng phần tử bằng nhau), và mỗi luồng tính toán trong từng đoạn riêng biệt.
- Lưu các số 2 -> N vào một mảng chung, nếu một luồng nào đấy rảnh sẽ lấy ra một số trong mảng đấy để kiểm tra, nếu là số nguyên tố thì thêm nó vào một mảng chứa các số nguyên tố (mảng này cũng được chia sẻ giữa các luồng).

Về cân bằng tải giữa luồng: Ta dễ thấy rằng nếu số càng lớn thì khối lượng tính toán để kiểm tra xem số đó có là số nguyên tố hay không càng lớn, vì vậy với cách chia thứ nhất, những luồng xử lý trên dãy các số nguyên bé sẽ hoàn thành công việc sớm hơn, và những luồng về sau sẽ càng mất nhiều thời gian để tính toán hơn, cho dù số phần tử của mỗi đoạn là bằng nhau. Do đó, ta thấy rằng cách chia thứ nhất cân bằng tải giữa các luồng không được tốt.

Với cách chia thứ hai, các luồng sẽ luân phiên nhau lấy ra một gía trị trong mảng chung, kiểm tra tính nguyên tố của gía trị đó một cách độc lập, sau khi hoàn thành công việc sẽ lấy một gía trị khác để kiểm tra, ta thấy rằng công việc được phân bố đều giữa các luồng, vì vậy cách chia thứ hai cho ta cân bằng tải tốt hơn.

Về đồng bộ luồng: Ở đây ta xét cách chia thứ hai, các luồng sẽ chia sẻ 2 tài nguyên chung đó là mảng các số 2 -> N và mảng chứa các số nguyên tố. Ta cần đảm bảo tại mỗi thời điểm chỉ có duy nhất một luồng được truy cập tài nguyên chung, nếu luồng khác muốn truy cập phải đợi (block) cho đến khi luồng trước đó cập nhật xong. Python cung cấp cho chúng ta các class cơ bản để thực hiện đồng bộ luồng bao gồm: `Lock, RLock, Condition, Event, Semaphore,...`

## Lock

Lock là cơ chế đồng bộ cơ bản nhất của Python. Một Lock gồm có 2 trạng thái, `locked` và `unlocked`, cùng với 2 phương thức để thao tác với Lock là `acquire()` và `release()`. Các quy luật trên Lock là:

- Nếu trạng thái (state) là `unlocked`, gọi `acquire()` sẽ thay đổi trạng thái sang `locked`
- Nếu trạng thái là `locked`, tiến trình gọi `acquire()` sẽ phải đợi (block) cho đến khi tiến trình khác gọi method `release()`.
- Nếu trạng thái là `unlocked`, gọi method `release()` sẽ phát ra RuntimeError exception.
- Nếu trạng thái là `locked`, gọi method `release()` sẽ chuyển trạng thái của Lock sang `unlocked`.

Tại mỗi thời điểm, chỉ có nhiều nhất một thread sở hữu `Lock`. Với cơ chế Lock, ta có thể đồng bộ bài toán đếm số nguyên tố như sau:

```python
import math
import threading

def is_prime(n):
	"""Check if n is prime or not
    """
    root = int(math.sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            return False
    return True

class CountPrime(threading.Thread):

    def __init__(self, list_num, list_lock, out_lock, output):
        threading.Thread.__init__(self)
        self._list = list_num	# list of number from 2 to N
        self._list_lock = list_lock	# Lock for list_num
        self._out_lock = out_lock	# Lock for output
        self._output = output	# list of prime numbers

    def run(self):
        while True:
        	# request to access shared resource
            # if there are many threads acquiring Lock, only one thread get the Lock
            # and other threads will get blocked
            self._list_lock.acquire()
            try:
                n = next(self._list)	# pop a number in list_num
            except StopIteration:
                return
            finally:
            	# release the Lock, so other thread can gain the Lock to access list_num
                self._list_lock.release()

            if not is_prime(n):
                continue

            self._out_lock.acquire()
            self._output.append(n)
            self._out_lock.release()

def parallel_primes(n, num_threads=None):
    """Parallel count number of prime from 2 to n

    Count prime numbers from 2 to n using num_threads threads
    If num_threads is None, using os.cpu_count()

    """
    list_num = (i for i in range(2, n + 1))
    list_lock = threading.Lock()
    out_lock = threading.Lock()
    output = []
    threads = []

    if num_threads is None:
        try:
            num_threads = os.cpu_count()
        except AttributeError:
            num_threads = 4

    elif num_threads < 1:
        raise ValueError('num_threads must be > 0')

    for i in range(num_threads):
        thread = CountPrime(list_num, list_lock, out_lock, output)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return output

```




[Source](https://viblo.asia/p/lap-trinh-da-luong-cac-co-che-dong-bo-trong-python-OEqGj6bQG9bL)