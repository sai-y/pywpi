#!/usr/bin/python3

import threading

def thread_function(string):
  for num in range(5):
    print("%s: Iteration: %d" %(string, num))

if __name__ == '__main__':
  thread_1 = threading.Thread(target=worker, args=("Thread 1",))
  thread_1.start()

  thread_2 = threading.Thread(target=worker, args=("Thread 2",))
  thread_2.start()

  thread_3 = threading.Thread(target=worker, args=("Thread 3",))
  thread_3.start()