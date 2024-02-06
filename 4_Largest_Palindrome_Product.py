import math


def isPalindrome(number):
    num = str(number)
    for i in range(0, math.floor(math.log10(number)) + 1):
        if num[i] != num[len(num) - i - 1]:
            return False
    return True


largest = 0
for i in range(100, 999):
    for j in range(100, 999):
        if isPalindrome(i * j) and i * j > largest:
            largest = i * j
print(largest)
