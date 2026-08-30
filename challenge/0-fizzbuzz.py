#!/usr/bin/python3
import sys

def fizzbuzz(n):
    if n < 1:
        return

    tmp = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            tmp.append("FizzBuzz")
        elif i % 3 == 0:
            tmp.append("Fizz")
        elif i % 5 == 0:
            tmp.append("Buzz")
        else:
            tmp.append(str(i))
            
    print(" ".join(tmp))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        sys.exit(1)

    fizzbuzz(int(sys.argv[1]))
