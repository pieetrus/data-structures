def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer'
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


def fib(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer'
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer'
    if n == 0:
        return 0
    return int(n % 10) + sumOfDigits(int(n//10))


def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'The exp must be positive integer'
    if exp == 0:
        return 1
    if exp == 1:
        return base

    return base * power(base, exp - 1)


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be positive integer'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a % b)
