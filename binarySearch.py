"""
Basic Logic:
Split array in two (ordered array) 
if midpoint < serachterm, search left subtree
otherwise, search right subtree
"""

list_to_search = [1, 2, 4, 6, 8, 34, 56, 876, 9393]

"""def binary_search(array, search_term) :
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
        
        iteration = iteration + 1"""

"""
Baisc logic
split array = two
search teh right sub tree by setting left or right to equal midpoint +- 1
repeat till item found or iterations > len(list)
1234 5 6 7
"""

def binary_search(array, searchTerm) :
    loop = True
    i = 0
    left = 0
    right = len(array) - 1

    while loop == True:
        midpoint = int((left+right)/2)

        if array[midpoint] < searchTerm :
            # Search right subtree
            left = midpoint + 1
        elif array[midpoint] > searchTerm :
            # Search left subtree
            right = midpoint - 1
        else :
            print ("Item found at " + str(midpoint))
            loop = False

        i = i + 1

        if i > len(array) :
            print ("Item not found")
            loop = False 

binary_search(list_to_search, 10000)