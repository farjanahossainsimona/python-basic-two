def add(a, b, c):
    return a+b+c


def multiply(a, b, c):
    return a*b*c


# temp = add(1, 2, 3)
# print(temp)

# mltpl = multiply(1, 2, 4)
# print(mltpl)


def print_my_name(myname):
    # This will print the given name
    # print('The given name is', myname)
    if myname == "Simona":
        return True
    else:
        return False


name = print_my_name('Bd')

if name:
    print('This is my name')
else:
    print('This is not my name')


def counter(num):
    print(num)
    num += 1
    counter(num)


counter(1)
