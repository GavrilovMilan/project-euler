sum, first, second = 0, 1, 2
while second < 4000000:
    if second % 2 == 0:
        sum = sum + second
    second = second + first
    first = second - first
print(sum)