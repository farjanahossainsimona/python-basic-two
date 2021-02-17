print('Please input your number:')
number = int(input())
temp = number
while number > 1:
    number = number - 1
    temp = temp * number
    print(temp)
if number == 0:
    print(1)
else:
    print(temp)
