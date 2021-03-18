import sys
try:
    print(10/0)
except ZeroDivisionError:
    print(sys.exc_info())
