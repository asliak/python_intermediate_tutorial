import threading

def helloworld():
    print("Hello World!")

t0 = threading.Thread(target = helloworld)
t0.start()

def function1():
    for x in range(10):
        print("ONE")

def function2():
    for x in range(10):
        print("TWO")

t1 = threading.Thread(target = function1)
t2 = threading.Thread(target = function2)

t1.start()
t2.start()

def hello():
    for x in range(20):
        print("Hello!")

t3 = threading.Thread(target = hello)
t3.start()
t3.join()

print("Another Text") # will be printed before threadings
# if the .join at the upper line does not exist


