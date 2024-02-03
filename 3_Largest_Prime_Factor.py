def primeFactor(number):
    largest = 1
    num = number
    i = 2

    while num > 1 and i < num:
        if num % i == 0:
            largest = i
            num = num // i
        i += 1
    return largest


# 13195
# 600851475143

num = 124
print(primeFactor(num))

num = 600851475143
print(primeFactor(num))
