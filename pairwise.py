def sum_index(arr: list, sum: int):
    
    n = 1
    m = 0
    total = []
    sum1 = 0
    sum2 = 0
    index1 = 0
    index2 = 0

    for i in range(0, len(arr) - 1):
        
        while(n < len(arr) - m):

            sum1 = arr[i]
            sum2 = arr[i+n]

            if sum1 + sum2 == sum:
                index1 = arr.index(sum1, i)
                index2 = arr.index(sum2, i)

                total.append(index1 + index2)
            
            n += 1

        n = 1    
        m += 1
    
    import functools
    return functools.reduce(lambda num1, num2: num1 + num2, total)

def pairwise(arr: list, sum: int):

    pair = []

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum and not (i in pair) and not (j in pair):
                pair.append(i)
                pair.append(j)
    
    import functools

    return functools.reduce(lambda sum1, sum2: sum1 + sum2, pair)


print(pairwise([0, 0, 0, 0, 1, 1], 1))