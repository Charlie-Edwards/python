# made for fun since i know a bit of chinese

english = input().lower()

words = english.split()

for word in words:
    if word == "hi" or word == "hello":
        print("mi hao", end=" ")
    elif word == "i" or word == "im" or word == "my":
        print("wo", end=" ")
    elif word == "is" or word == "are":
        pass
    elif word == "name" or word == "called":
        print("jiao", end=" ")
    elif word == "you" or word == "your" or word == "youre":
        print("ni", end=" ")
    elif word == "yes":
        print("dui", end=" ")
    elif word == "no":
        print("bu", end=" ")
    elif word == "1" or word == "one":
        print("yi", end=" ")
    elif word == "2" or word == "two":
        print("er", end=" ")
    elif word == "3" or word == "three":
        print("san", end=" ")
    elif word == "4" or word == "four":
        print("si", end=" ")
    elif word == "5" or word == "five":
        print("wu", end=" ")
    elif word == "6" or word == "six":
        print("liu", end=" ")
    elif word == "7" or word == "seven":
        print("qi", end=" ")
    elif word == "8" or word == "eight":
        print("bai", end=" ")
    elif word == "9" or word == "nine":
        print("jiu", end=" ")
    elif word == "10" or word == "ten":
        print("shi", end=" ")
    elif word == "happy":
        print("gaoxing", end="")
    else:
        print(word, end=" ")
