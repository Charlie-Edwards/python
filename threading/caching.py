from functools import cache
import sys
import time
import threading

@cache
def fibonacci(n):
    n = int(n)
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(sys.argv[1])

start = time.time()

thread = threading.Thread(target=fibonacci, args=(n,))
thread.start()
thread.join()

end = time.time()
print(end - start)
