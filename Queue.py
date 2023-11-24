from queue import Queue
my_qu = Queue()
my_qu.put(1)
my_qu.put(2)
my_qu.put(3)
print(my_qu.empty())
print(my_qu.qsize())
my_qu.queue.clear()
print(my_qu.empty())