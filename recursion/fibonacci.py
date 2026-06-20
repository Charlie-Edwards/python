def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonacci(0))   # 0
print(fibonacci(5))   # 5
print(fibonacci(10))  # 55
print(fibonacci(50))  # 12586269025

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
