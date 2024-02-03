import math


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primeFactor(num):
    largest = 1
    c = num
    i = 2

    while c > 1:
        if c % i == 0:
            largest = i
            c = c // i
        i += 1
    return largest


# 13195
# 600851475143

num = 13195
print(primeFactor(num))

num = 600851475143
print(primeFactor(num))
