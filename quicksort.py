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

partition:
    pick a pivot point
    swap rightmost element and pivot point
    get value of left

    for every item in range
        if array[i] >< pivot_value:
            swap array[i] and pivot value
            increment store position
        
    swap pivot value and stor position
    RETURN STORE POSITION

quicksort:
    if left < right:
        p = partition()
        quicksort left and right

"""

def partition(array, left, right) :
    pivot = int((left+right)/2)
    pivot_value = array[pivot]

    # Swap rightmost element and pivot point
    array[pivot] = array[right]
    array[right] = pivot_value

    # Set store position
    store_position = left

    # For every element
    for i in range(left, right) :
        # If it needs to be swapped
        if array[i] > pivot_value :
            # Swap array with store position value
            temp = array[store_position]
            array[store_position] = array[i]
            array[i] = temp

            # Increment store position
            store_position = store_position + 1
    
    # Swap pivot and store_position
    temp = array[store_position]
    array[store_position] = pivot_value
    array[right] = temp

    return store_position

def quicksort(array, left, right) :
    if left < right :
        p = partition(array, left, right)
        # Quicksort left sub list
        quicksort(array, left, p-1)
        # Quicksort right sub list
        quicksort(array, p+1, right)



listToSort = [1, 3, 2, 6, 34, 58, 2763, 6, 4, 7, 8, 3]
quicksort(listToSort, 0, len(listToSort) - 1)

print(listToSort)
