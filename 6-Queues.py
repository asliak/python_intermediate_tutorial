import queue 
# FIRST IN FIRST OUT
#q = queue.Queue()
#
#numbers = [10, 20, 30, 40, 50, 60, 70]
#for number in numbers:
#    q.put(number)
#
#print(q.get())
#print(q.get())

# STARTING FROM THE LAST ELEMENT
#q = queue.LifoQueue()
#
#numbers = [1,2,3,4,6,7]
#for x in numbers:
#    q.put(x)
#
#print(q.get())

# PRIORITY QUEUE

q = queue.PriorityQueue()
# lower the number higher the priority
q.put((2, "Hello World!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get()[1])


