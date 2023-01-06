'''
The bubble sort method starts at the beginning of an unsorted array and 'bubbles up' 
unsorted values towards the end, iterating through the array until it is completely sorted. 
It does this by comparing adjacent items and swapping them if they are out of order. 
The method continues looping through the array until no swaps occur at which point the array is sorted.
'''
import time

def bubble_sort(array: list):

    start = time.time()

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if not array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    
    end = time.time()
    print(f"Execution time: {(end - start)}")

    return array

print(bubble_sort([1, 2, 4, 6, 3, 55, 64, 34, 12, 43, 89, 134, 567, 453, 12334, 5678, 5642])) 