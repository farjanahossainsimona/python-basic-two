# trial division prime number
def is_prime(n):
    if n <= 1:
        raise ValueError('The number must be greater than 1.')
    elif n <= 3:
        return True
    elif (n % 2) == 0 or (n % 3) == 0:
        return False
    else:
        i = 5
        while (i * i) <= n:
            if (n % i) == 0 or (n % i+2) == 0:
                return False
            i = i + 6
        return True


n = int(input("Enter a number: "))

if is_prime(n):
    print(n, 'is a prime number')
else:
    print(n, 'is a composite number')
