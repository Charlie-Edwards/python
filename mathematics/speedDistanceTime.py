import sys

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def find():
    global find_speed, find_distance, find_time, find_nothing
    if speed == "?":
        find_speed = True
        print("Finding speed...\n")
    elif distance == "?":
        find_distance = True
        print("Finding distance...\n")
    elif time == "?":
        find_time = True
        print("Finding time...\n")
    else:
        find_nothing = True
        print("Finding nothing...\n")

def unit_separation():
    s, d, t = '', '', ''
    su, du, tu = '', '', ''

    if not find_speed:
        s_list = []
        s_unit = []

        for char in speed:
            if char in numbers:
                s_list.append(char)
            else:
                s_unit.append(char)

        for digit in s_list:
            s += digit

        for digit in s_unit:
            su += digit

    if not find_distance:
        d_list = []
        d_unit = []

        for char in distance:
            if char in numbers:
                d_list.append(char)
            else:
                d_unit.append(char)

        for digit in d_list:
            d += digit

        for digit in d_unit:
            du += digit

    if not find_time:
        t_list = []
        t_unit = []

        for char in time:
            if char in numbers:
                t_list.append(char)
            else:
                t_unit.append(char)

        for digit in t_list:
            t += digit

        for digit in t_unit:
            tu += digit

    return s, su, d, du, t, tu

def solve():
    global s, d, t
    if find_speed:
        s = float(d) / float(t)
    elif find_distance:
        d = float(s) * float(t)
    elif find_time:
        t = float(s) / float(d)

try:
    speed = sys.argv[1]
    distance = sys.argv[2]
    time = sys.argv[3]

except IndexError:
    print("Use: speedDistanceTime.py s d t")
    print("eg: py speedDistanceTime.py ? 100m 5s\n")
    speed = "?"
    distance = "100m"
    time = "5s"

find_speed, find_distance = False, False
find_time, find_nothing = False, False

find()
s, su, d, du, t, tu = unit_separation()
solve()

if find_speed:
    su = f"{du}/{tu}"
elif find_distance:
    du = su.split('/')[0]
elif find_time:
    tu = su.split('/')[1]
else:
    pass

print(f"Speed: {int(s) if float(s) % 1 == 0 else float(s)}{su}")
print(f"Distance: {int(d) if float(d) % 1 == 0 else float(d)}{du}")
print(f"Time: {int(t) if float(t) % 1 == 0 else float(t)}{tu}")
