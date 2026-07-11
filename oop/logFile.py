def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logFile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"Output: {fname} function returned value {value}\n")
        return value
    
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10, 20))
