"""
Basic Logic:
Split array in two (ordered array) 
if midpoint < serachterm, search left subtree
otherwise, search right subtree
"""

list_to_search = [1, 2, 4, 6, 8, 34, 56, 876, 9393]

def binary_search(array, search_term) :
    left = 0
    right = len(array)
    itemFound = False
    iteration = 0

    while itemFound == False:
        midpoint = int((left+right)/2)

        if array[midpoint] > search_term:
            # Search left side of array
            right = midpoint - 1
        elif array[midpoint] < search_term:
            # Search right side of array
            left = midpoint + 1
        elif array[midpoint] == search_term:
            itemFound = True
            print ("Item has been found")
            print (midpoint)

        if iteration > len(array) :
            itemFound = True
            print ("Item is not in array")
        
        iteration = iteration + 1

