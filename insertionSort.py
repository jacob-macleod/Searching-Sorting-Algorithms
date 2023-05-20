listToSort = [1, 3, 2, 6, 34, 58, 2763, 6, 4, 7, 8, 3]

"""def insertion_sort(list):
    for p in range(1, len(list)) :
        hole = list[p]
        z = p

        while z > 0 and list[z-1] > hole:
            list[z] = list[z-1]
            z = z -1
        
        list[z] = hole

    return list"""



def insertion_sort(array) :
    for p in range(1, len(array)) :
        hole = array[p]
        z = p

        while z > 0 and array[z-1] > hole :
            array[z] = array[z-1]
            z = z-1

        array[z] = hole
    return array

print (insertion_sort(listToSort))
