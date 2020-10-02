import threading
import math

def target_func(data):
  thread_id = threading.get_ident()
  print(f'Thread {thread_id} with data: {data}')

class WorkerThread(threading.Thread):
  def __init__(self, data):
    super().__init__()
    self.data = data
  def run(self):
    # This method is invoked when starting a thread
    # Do the work of thread here
    print(f'Thread {self.ident} is running with data: {self.data}')


if __name__ == '__main__':
  a = 'goodkat'
  b = 'godfather'

  # Create thread by passing target_func to target param
  thread1 = threading.Thread(target = target_func, args=(a,))
  thread2 = WorkerThread(b)

  thread1.start()
  thread2.start()

  # Wait for thread 1, thread 2, to terminate
  thread1.join()
  thread2.join()

  print('Main thread exited')

# Output:
# Thread 140280251209472 is running with data: goodkat
# Thread 140280242816768 is running with data: godfather
# Main thread exited