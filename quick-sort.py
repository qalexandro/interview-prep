'''
Quick sort is an efficient, recursive divide-and-conquer approach to sorting an array. 
In this method, a pivot value is chosen in the original array. 
The array is then partitioned into two subarrays of values less than and greater than the pivot value. 
We then combine the result of recursively calling the quick sort algorithm on both sub-arrays. 
This continues until the base case of an empty or single-item array is reached, which we return. 
The unwinding of the recursive calls return us the sorted array.
'''

def partition_index(array: list, low_index: int, high_index: int):

    pivot = array[high_index]
    greater_index = low_index - 1

    for i in range(low_index, high_index):
        if array[i] <= pivot:
            greater_index = greater_index + 1
            (array[greater_index], array[i]) = (array[i], array[greater_index])
    
    (array[greater_index + 1], array[high_index]) = (array[high_index], array[greater_index + 1])

    return greater_index + 1


def recursive_sort(array: list, low_index: int, high_index: int):

    if low_index < high_index:

        pivot_index = partition_index(array, low_index, high_index)
        recursive_sort(array, low_index, pivot_index - 1)
        recursive_sort(array, pivot_index + 1, high_index)

def quick_sort(array: list):

    low_index = 0
    high_index = len(array) - 1

    recursive_sort(array, low_index, high_index)

    return array

print(quick_sort([2, 5, 6, 7, 34, 54, 21]))