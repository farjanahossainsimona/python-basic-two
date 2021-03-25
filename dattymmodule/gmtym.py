import time
t = time.gmtime()
print(t)
# strftime:tupple to string!
st = time.strftime('%I:%M:%S %p %d %B %Y', t)
print(st)
