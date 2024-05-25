#here you can find gcd of any two integers

def gcd(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return None

    if a == 0 and b == 0:
        return None
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

#in case you forgot the fibonacci numbers

def fibonacci(f):
    if not isinstance(f, int) or f < 0:
        return None

    if f == 0 or f == 1:
        return 1
    else:
        return fibonacci(f - 1) + fibonacci(f - 2)