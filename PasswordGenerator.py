#Create a program that creates strong, random passwords

import random

def randGen():
    #length
    length = random.randint(10, 20)
    pw = ""

    for x in range(length):
        c = random.randint(1,2)
        if c == 1:
            a = random.randint(0,9)
            a = str(a)
        else:
            a = random.randint(97, 122)
            a = chr(a)
            a = str(a)
        pw+=a
    return pw


def main():
    input("Press enter to generate a new random password")
    print(randGen())
main()
