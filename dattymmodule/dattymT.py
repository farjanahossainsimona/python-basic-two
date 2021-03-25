from datetime import time
t = time(5, 15, 00)
# print(t)
# h = t.hour
# print(h)
# m = t.minute
# print(m)
# s = t.second
# print(s)
rt = t.replace(3, 30, 45)
print(rt)
st = rt.strftime('%I:%M:%S')
print(st)
