# Linearly go through list. If the next variable is smaller than the previous one, swap them

listToSort = [1, 3, 2, 6, 34, 58, 2763, 6, 4, 7, 8, 3]
""" Example program
def bubble_sort(list) :
    swapped = True

    while swapped is True:
        swapped = False
        for i in range(1, len(list)) :
            if list[i] < list[i-1] :
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
                swapped = True

    print (list)"""


"""
Basic idea
Do a while loop
    swapped = false
    for each element, if it and the revious one need to be swapped, swap them and swapped = true
    if swapped = false, loop = false
"""

def bubble_sort(list) :
    loop = True

    while loop == True:
        swapped = False

        for i in range (1, len(list)) :
            if list[i] > list[i-1] :
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
                swapped = True

        if swapped == False :
            loop = False

    return list

print (bubble_sort(listToSort))