class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)
    
    def __repr__(self):
        return f"\n+----------+----------+\n\
| X: {a:<5} | Y: {b:<5} |\n\
+----------+----------+\n\
| X: {c:<5} | Y: {d:<5} |\n\
+----------+----------+\n\
| X: {self.x:<5} | Y: {self.y:<5} |\n\
+----------+----------+"

a = float(input("Vector 1 (x): "))
b = float(input("Vector 1 (y): "))
c = float(input("Vector 2 (x): "))
d = float(input("Vector 2 (y): "))

method = input("Method: ")

v1 = Vector(a, b)
v2 = Vector(c, d)

if method == "add" or method == "a":
    v3 = v1 + v2
elif method == "sub" or method == "s":
    v3 = v1 - v2
elif method == "mul" or method == "m":
    v3 = v1 * v2
elif method == "div" or method == "d":
    v3 = v1 / v2

print(v3)
