# Greatest common Divisor(GDC)
def gcd(a, b):
    if b > a:
        gcd(b, a)

    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


print("print input two integers:")
a, b = map(int, input().split())
print(gcd(a, b))
