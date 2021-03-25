# from datetime import date
# d = date(2021, 3, 25)
# print(d)
from datetime import date
t = date.today()
# y = t.year
# print(y)
# m = t.month
# print(m)
# d = t.day
# print(d)
# t = t.replace(2021, 5, 23)
st = t.strftime('%d %b, %Y')
st1 = t.strftime('%d %B, %y')
print(st)
print(st1)
