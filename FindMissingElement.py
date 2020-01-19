import collections

def finder1(arrA, arrB):

    arrA.sort()
    arrB.sort()

    for num1, num2 in zip(arrA, arrB):
        if num1 != num2:
            return num1
    
    return arrA[-1]

def finder2(arrA, arrB):

    d = collections.defaultdict(int)

    for num in arrB:
        d[num] += 1

    for num in arrA:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

def finder3(arrA, arrB):
    result = 0

    for num in arrA+arrB:
        result^=num
    
    return result
        

print(finder3([1,2,3], [3,2]))