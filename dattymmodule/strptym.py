# import time
# st = time.strptime("30 Nov 00", "%d %b %y")
# print(st)
import time
st = time.strptime("30 Oct 2000", "%d %b %Y")
print(st)
y = st.tm_year
print(y)
print(st[0])
m = st.tm_mon
print(m)
print(st[1])
md = st.tm_mday
print(md)
print(st[2])
