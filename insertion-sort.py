'''
This method works by building up a sorted array at the beginning of the list. 
It begins the sorted array with the first element. 
Then it inspects the next element and swaps it backwards into the sorted array until 
it is in sorted position. 
It continues iterating through the list and swapping new items backwards into the sorted portion 
until it reaches the end. 
This algorithm has quadratic time complexity in the average and worst cases.
'''


def insertion_sort(arr: list):

    sorted = []

    for element in arr:
        sorted.append(element)

        for i in range(0, len(sorted)):
            for j in range(i + 1, len(sorted)):
                if not sorted[i] < sorted[j]:
                    temp = sorted[i]
                    sorted[i] = sorted[j]
                    sorted[j] = temp
    
    return sorted

print(insertion_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))