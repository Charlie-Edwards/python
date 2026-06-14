import threading
import time

cat = ""
killswitch = False

def readFile():
    global cat
    while killswitch == False:
        with open("filetoreadfrom.txt", "r") as file:
            cat = file.read()

def printFile():
    global cat
    print("Edit filetoreadfrom.txt while the program is running and watch the text change in the output.")
    time.sleep(1)
    print("The program will run for 60 seconds so be quick.")
    time.sleep(2)
    t3.start()
    while killswitch == False:
        print(cat)

def timer():
    global killswitch
    time.sleep(60)
    killswitch = True

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printFile)
t3 = threading.Thread(target=timer, daemon=True)

t1.start()
t2.start()
