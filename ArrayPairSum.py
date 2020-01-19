def arrayPairSum(arr, sum):
    if len(arr) < 2:
        return
    
    seen = set()
    output = set()

    for num in arr:
        
        target = sum-num

        if target not in seen:
            seen.add(num)

        else:
           output.add((min(num, target), max(num, target)))

    # print("\n".join(map(str, list(output))))
    return len(output) 


print(arrayPairSum([1, 3, 2, 2, 5], 4))
