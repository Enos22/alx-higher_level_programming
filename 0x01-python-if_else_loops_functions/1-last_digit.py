#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# the find_last function below finds the last digit of the number


def find_last2(num):
    temp = str(num)
    last = int(temp[len(temp) - 1])
    if num < 0:
        return last * -1
    return last


def find_last(num):
    if num < 0:
        return -1 * ((-1 * num) % 10)
    return (num % 10)


last_num = find_last(number)
if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
