# Select pivot
# Swap pivot with rightmost value
# Store position of leftmost value as store_position
# For each item, if it is < pivot, swap it with the store position
# Swap the pivot and the store_postion

listToSort = [1, 3, 2, 6, 34, 58, 2763, 6, 4, 7, 8, 3]

"""def partition(array, left, right):
    pivot = int((left + right) / 2)
    pivot_value = array[pivot]
    array[pivot] = array[right]
    array[right] = pivot_value
    store_position = left
    for i in range(left, right):
        if array[i] < pivot_value:
            temp = array[i]
            array[i] = array[store_position]
            array[store_position] = temp
            store_position += 1
    temp = array[store_position]
    array[store_position] = array[right]
    array[right] = temp
    return store_position

def quicksort(array, left, right):
    if left < right:
        p = partition(array, left, right)
        quicksort(array, left, p - 1)
        quicksort(array, p + 1, right)""" 

"""
Basic logic

Partition
    set pivot and pivot value - midpoint
    swap rightmost element with pivot
    set store position = left most

    for every elemebt in array
        if array[i] < element 
            swap element and store position
            increment storeposition
    
    swap right and store position
    return store position

quicksort
    if left < right
    partition
    quicksort right and left subtree
"""


"""
Partition
    set pivot and pivot value
    swap righta dn pivot 
    set storeposition = left

    of each element
        if element < pivot value
            swap selement and store position
            increment store position
    
    swap right and store position
    return pivot

quicksort
    if left < right
        p = parition
        quicksort left and right
"""

def partition(left, right, array) :
    pivot = int((left+right) / 2)
    pivot_value = array[pivot]

    array[pivot] = array[right]
    array[right] = pivot_value

    store_position = left

    for i in range(left, right) :
        if array[i] < pivot_value :
            temp = array[i]
            array[i] = array[store_position]
            array[store_position] = temp
            store_position = store_position + 1
    
    # Swap rightmost and store position
    temp = array[right]
    array[right] = array[store_position]
    array[store_position] = temp

    return store_position

def quicksort(left, right, array) :
    if left<right:
        p = partition(left, right, array)
        quicksort(left, p-1, array)
        quicksort(p+1, right, array)

quicksort(0, len(listToSort)-1, listToSort)
print (listToSort)