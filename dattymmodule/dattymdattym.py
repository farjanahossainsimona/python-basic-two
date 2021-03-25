# from datetime import datetime
# t = datetime.today()
# print(t)
# t1 = datetime.now()
# print(t1)
# t2 = datetime.utcnow()
# print(t2)
# d = t2.year
# print(d)

# dtdt = '05:15:00 AM 23 october, 1996'
# fo = datetime.strptime(dtdt, '%I:%M:%S %p %d %B, %Y')
# print(fo)

# t = datetime.now()
# print(t)
# rt = t.replace(year=2001, month=10, day=23, hour=5, minute=14)
# print(rt)
# strt = t.strftime('%I:%M:%S %p %d %B, %Y')
# print(strt)
from datetime import datetime, date, time
my_date = date(1997, 10, 23)
my_time = time(5, 15, 00)
c = datetime.combine(my_date, my_time)
print(c)
