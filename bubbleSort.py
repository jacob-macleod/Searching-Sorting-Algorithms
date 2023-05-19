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




# Basic logic
# Go through list linearly, starting at n=1
# If the item is smaller than the previous one, swap them
# Repeat while swapped = True, at start of each iteration swapped = false, swapped = true when swap happens

def bubble_sort(list) :
    swapped = True

    while swapped == True:
        swapped = False

        for i in range(1, len(list)) :
            if list[i] < list[i-1] :
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp
                swapped = True

    return list

print (bubble_sort(listToSort))
