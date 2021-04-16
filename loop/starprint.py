# *******
# *******
# *******
# *******
# *******
# *******
number = int(input('Please input the number:'))
temp = number
while number > 0:
    count = temp
    while count > 0:
        print('*', end='')
        count -= 1
    print()
    number -= 1


# *
# **
# ***
# ****
# *****
number = int(input('Please input the number:'))
i = 1
while i <= number:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1


# *****
# ****
# ***
# **
# *
number = int(input('Please input the number:'))
i = 1
while i <= number:
    j = number
    while j >= i:
        print('*', end='')
        j -= 1
    print()
    i += 1
