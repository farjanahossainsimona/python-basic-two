def add(**kwargs):
    print(type(kwargs))
    print(kwargs)
    tmp = 0
    for i in kwargs:
        tmp = tmp + kwargs[i]
    # print(tmp)
    return tmp


temp = add(a=1, b=2, c=3, d=4)
print(temp)

dics = {'a': 1, 'b': 82, 'c': 3, 'd': 48}
print(dics['b'])
