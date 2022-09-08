# Missing number in list from 0 to 100

def findMissing(list, n):
    sum1 = n*(n+1)/2
    sum2 = sum(list)
    print(sum1 - sum2)

# Two sum


def twoSum(list, target):
    for i in range(len(list)):
        for j in range(1, len(list)):
            if list[i] + list[j] == target:
                return (list[i], list[j])


# Max product of two integers in list all numbers positive

def findMaxProduct(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result = max(result, nums[i] * nums[j])
            pairs = str(nums[i]) + ", " + str(nums[j])
    print(pairs)
    return result


def isUnique(list):
    hashset = set()
    for item in list:
        if item in hashset:
            return False
        else:
            hashset.add(item)
    return True


def isPermutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


matrix = [[1, 2], [3, 4]]


def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1


print(matrix)
print(rotate_matrix(matrix))
