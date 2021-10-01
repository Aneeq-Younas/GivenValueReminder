def div(num):
    a = num // 100
    b = a

    while a > 0:
        a /= 100
        b += int(a)

    return b


print("The reminder of given value is: ", (div(500)))
print("The reminder of given value is: ", (div(1500)))
print("The reminder of given value is: ", (div(6500)))
