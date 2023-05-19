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

"""Basic Logic

Partition:
    Get the middle value of the array (this can also be a random value)
    Get the value of this (pivot_value)
    swap the pivot and the rightmost element
    store the index of the leftmost position

    for every element in the range,
    if it is bigger than the pivot_value then:
        swap it with the element at store position and increment store position

    swap the rightmost element and store position and return store_position


quicksort:
    recursively search sub sections
    if left< right (otherwise the list must be sorted), this is the base clause
        p = partition
        quicksort the left side and right side, left and right p -1 or +1 respectively
"""

def partition(array, left, right) :
    pivot = int((left+right)/2)
    pivot_value = array[pivot]

    # Swap the pivot and the rightmost element
    temp = array[pivot]
    array[pivot] = array[right]
    array[right] = temp

    # Store the index of the leftmost position
    store_position = left

    for i in range(left, right) :
        if array[i] < pivot_value:
            # Swap it with the element at store position
            temp = array[i]
            array[i] = array[store_position]
            array[store_position] = temp

            # Increment the store position
            store_position = store_position + 1

    # Swap it rightmost element with store position
    temp = array[store_position]
    array[store_position] = array[right]
    array[right] = temp

    # Return store position
    return store_position

def quicksort(array, left, right) :
    if left < right:
        p = partition(array, left, right)
        quicksort(array, left, p-1)
        quicksort(array, p+1, right)


listToSort = [1, 3, 2, 6, 34, 58, 2763, 6, 4, 7, 8, 3]
quicksort(listToSort, 0, len(listToSort) - 1)

print(listToSort)
