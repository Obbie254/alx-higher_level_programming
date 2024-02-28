#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 100):
        if num % 3 == 0 and num % 5 == 0:
            print("{}".format("FizzBuzz"), end=' ')
            continue
        elif num % 3 == 0:
            print("{}".format("Fizz"), end=' ')
            continue
        elif num % 5 == 0:
            print("{}".format("Buzz"), end=' ')
            continue
        print("{}".format(num), end=' ')
