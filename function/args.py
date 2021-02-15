def add(*argss):
    print(type(argss))
    tmp = 0
    for number in argss:
        # tmp = tmp + number
        tmp += number

    return tmp


temp = add(1, 2, 22, 12)
print(temp)


a = '1'
print(type(a))
