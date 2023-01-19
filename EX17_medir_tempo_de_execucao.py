import time

def calculate_time(func):
    def inner():
        start = time.time()

        func()

        end = time.time()

        return end - start
    
    return inner

@calculate_time
def test():
    for i in range(10000):
        print(i)
        for i in range(100000):
            pass

print(test())
