#f = open('firstFile.txt', 'r')
#content = f.read()
# print(content)
# f.close()

#f = open('firstFile.txt', 'w')
#content = f.write('21 february is international mother language day')
# print(content)
# f.close()

#f = open('firstFile.txt', 'a')
#content = f.write('21 february is international mother language day')
# print(content)
# f.close()

#f = open('firstFile.txt', 'r')
#content = f.read(5)
# print(content)
#content = f.read()
# print(content)
#p = f.tell()
# print(p)
#f.seek(0, 0)
#content = f.read()
# print(content)
# f.close()

with open('firstFile.txt', 'r') as f:
    content = f.read()
    print(content)
