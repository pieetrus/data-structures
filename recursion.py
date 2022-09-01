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


def decimalToBinary(n):
    assert int(n) == n, 'The number must be positive integer'
    if n == 0:
        return 0
    return n % 2 + 10 * decimalToBinary(int(n//2))


def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr


def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum


def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])


def stringifyNumbers(obj):
    for key in obj:
        if type(obj[key]) is dict:
            stringifyNumbers(obj[key])
        elif type(obj[key]) is int:
            obj[key] = str(obj[key])
    return obj


def collectStrings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is dict:
            result += collectStrings(obj[key])
        elif type(obj[key]) is str:
            result.append(obj[key])
    return result
