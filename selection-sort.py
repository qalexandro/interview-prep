'''
 Selection sort works by selecting the minimum value in a list and swapping it with the first value 
 in the list. It then starts at the second position, selects the smallest value in the remaining list, 
 and swaps it with the second element. 
 It continues iterating through the list and swapping elements until it reaches the end of the list. 
 Now the list is sorted. 
 Selection sort has quadratic time complexity in all cases.
'''
def selection_sort(arr: list):

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if min(arr[j:]) < arr[i]:
                temp = arr[i]
                arr[i] = min(arr[j:])

                index = arr[j:].index(min(arr[j:]))
                arr[index + j] = temp
    
    return arr

print(selection_sort([2, 4, 5, 1, 2, 3, 4]))